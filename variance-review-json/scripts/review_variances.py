"""Validate a location CSV and calculate a variance review. Standard library only.

Example from the variance-review folder:
python scripts/review_variances.py assets/location-pnl.csv references/policy.json

Prints JSON to stdout. Does not write files, edit Excel, call an API or generate prose.
"""
import argparse
import csv
from decimal import Decimal, InvalidOperation
import json

FIELDS = ('Location', 'Category', 'Period', 'Type', 'Budget', 'Actual')

def number(value, label):
    if value is None or isinstance(value, bool):
        raise ValueError(f'{label} must be a nonnegative finite number')
    try:
        result = Decimal(str(value))
    except InvalidOperation as exc:
        raise ValueError(f'{label} must be numeric') from exc
    if not result.is_finite() or result < 0:
        raise ValueError(f'{label} must be a nonnegative finite number')
    return result

def review(rows, policy):
    dollar = number(policy['dollar_threshold'], 'dollar threshold')
    pct = number(policy['percent_threshold'], 'percent threshold')
    if policy['comparison'] != 'strictly_greater_than':
        raise ValueError('Unsupported threshold comparison')
    period = str(policy['period'])
    if not rows:
        raise ValueError('No detail rows')
    seen, calculated = set(), []
    totals = {kind: {'budget': Decimal(0), 'actual': Decimal(0)} for kind in ('Revenue', 'Expense')}
    for index, row in enumerate(rows, 2):
        if any(field not in row for field in FIELDS) or None in row:
            raise ValueError(f'CSV row {index}: expected exactly the named columns')
        labels = {key: str(row[key] or '').strip() for key in FIELDS[:4]}
        if not all(labels.values()):
            raise ValueError(f'CSV row {index}: missing identifier')
        if labels['Period'] != period:
            raise ValueError(f'CSV row {index}: period does not match policy')
        kind = labels['Type']
        if kind not in totals:
            raise ValueError(f'CSV row {index}: Type must be Revenue or Expense')
        if labels['Location'].casefold() in ('total', 'grand total', 'subtotal'):
            raise ValueError('Supply detail rows only; totals are policy controls')
        key = tuple(labels[f].casefold() for f in FIELDS[:4])
        if key in seen:
            raise ValueError(f'CSV row {index}: duplicate location/category/period/type')
        seen.add(key)
        budget, actual = (number(row[f], f'CSV row {index} {f}') for f in ('Budget', 'Actual'))
        delta = actual - budget
        percent = delta / budget if budget else None
        # Cross-multiplication preserves strict boundaries without float rounding.
        material = abs(delta) > dollar or (budget > 0 and abs(delta) > pct * budget)
        impact = delta if kind == 'Revenue' else -delta
        direction = 'Favorable' if impact > 0 else 'Unfavorable' if impact < 0 else 'On plan'
        calculated.append({**labels, 'Budget': budget, 'Actual': actual, 'Variance': delta,
                           'VariancePercent': percent, 'Material': material,
                           'Direction': direction, 'ProfitImpact': impact})
        totals[kind]['budget'] += budget
        totals[kind]['actual'] += actual
    for kind, amounts in totals.items():
        for measure in ('budget', 'actual'):
            expected = number(policy[f'{kind.lower()}_{measure}_control'], f'{kind} {measure} control')
            if amounts[measure] != expected:
                raise ValueError(f'{kind} {measure} control mismatch: {amounts[measure]} vs {expected}')
        amounts['variance'] = amounts['actual'] - amounts['budget']
    material_rows = [r for r in calculated if r['Material']]
    material_rows.sort(key=lambda r: (0 if r['ProfitImpact'] < 0 else 1,
                                     -abs(r['ProfitImpact']), r['Location'], r['Category']))
    partial = {m: totals['Revenue'][m] - totals['Expense'][m] for m in ('budget', 'actual')}
    partial['variance'] = partial['actual'] - partial['budget']
    return {'entity': policy['entity'], 'period': period, 'currency': policy['currency'],
            'method': 'Python script', 'row_count': len(calculated), 'material_count': len(material_rows),
            'thresholds': {'dollars': dollar, 'percent': pct, 'comparison': 'strictly greater than; OR'},
            'controls_reconcile': True, 'totals': totals, 'partial_operating_result': partial,
            'material_rows': material_rows, 'all_rows': calculated}

def json_number(value):
    if isinstance(value, Decimal):
        return int(value) if value == value.to_integral_value() else float(value)
    raise TypeError(type(value).__name__)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('csv_path')
    parser.add_argument('policy_path')
    args = parser.parse_args()
    try:
        with open(args.csv_path, newline='', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            if reader.fieldnames != list(FIELDS):
                raise ValueError('CSV headers must be: ' + ', '.join(FIELDS))
            rows = list(reader)
        with open(args.policy_path, encoding='utf-8') as f:
            policy = json.load(f)
        result = review(rows, policy)
        print(json.dumps(result, default=json_number, indent=2, allow_nan=False))
    except (ValueError, KeyError, OSError) as exc:
        parser.exit(2, f'Review stopped: {exc}\n')

if __name__ == '__main__':
    main()
