import re

with open('input.txt', 'r') as file:
    input_data = file.read()

# Returns list when only one parenthese "(" return tuples when two parentheses "(())"
# pattern = r'\(\d+,\d+\)'
filterMul = r'mul\((\d+),(\d+)\)'

matches = re.findall(filterMul, input_data)

totalMulti = 0
count = 0

def mul(x, y):
    return int(x) * int(y)

for x, y in matches:
    totalMulti += mul(x, y)
    

print(totalMulti)