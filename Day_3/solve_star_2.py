import re

with open('input.txt', 'r') as file:
    input_data = file.read()


filterDo = r'do(.*?)don\'t'

firstFiltering = re.findall(filterDo, input_data)

filterMul = r'mul\((\d+),(\d+)\)'

finalMatches =  re.findall(filterMul, str(firstFiltering))

totalMulti = 0

def mul(x, y):
    return int(x) * int(y)

for x, y in finalMatches:
    totalMulti += mul(x, y)
    
    
print(firstFiltering)