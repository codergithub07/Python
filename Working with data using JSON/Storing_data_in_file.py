import json

numbers = [1, 2, 3, 4, 5]

file = 'numbers.json'

with open(file, 'w') as f:
    json.dump(numbers, f)