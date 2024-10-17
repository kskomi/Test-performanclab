import json

def fill_values(test_structure, value_map):
    for test in test_structure:
        if test['id'] in value_map:
            test['value'] = value_map[test['id']]
        
        if 'values' in test:
            fill_values(test['values'], value_map)

with open('values.json', 'r') as f:
    values_data = json.load(f)

value_map = {item['id']: item['value'] for item in values_data['values']}

with open('tests.json', 'r') as f:
    tests_data = json.load(f)

fill_values(tests_data['tests'], value_map)

with open('report.json', 'w') as f:
    json.dump(tests_data, f, indent=4)

print("Заполнение завершено, результат записан в report.json")
