from new_dummy_data import holdings, rules

def check_compliance(holdings, rules):
    violations = []

    for holding in holdings:
        for rule in rules:
            if rule['type'] == 'value_threshold':
                if holding['value'] > rule['threshold']:
                    violations.append({
                        'isin': holding['isin'],
                        'rule': 'value_threshold'
                    })
            elif rule['type'] == 'currency_blacklist':
                if holding['currency'] in rule['currencies']:
                    violations.append({
                        'isin': holding['isin'],
                        'rule': 'currency_blacklist'
                    })
    return violations

violations = check_compliance(holdings, rules)
print(f"{violations[0]["isin"]} violates the rule")
print(f"Current holdings that violate the rules: {violations}")