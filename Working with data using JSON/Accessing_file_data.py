import json

file = 'numbers.json'

with open(file) as f:
    numbers = json.load(f)
print(numbers)