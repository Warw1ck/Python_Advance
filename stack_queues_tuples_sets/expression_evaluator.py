from functools import reduce
data = input().split()
index = 0

operators = {'*': lambda i: reduce(lambda a, b: a*b, [int(num) for num in data[:i]]),
             '+': lambda i: reduce(lambda a, b: a+b, [int(num) for num in data[:i]]),
             '-': lambda i: reduce(lambda a, b: a-b, [int(num) for num in data[:i]]),
             '/': lambda i: reduce(lambda a, b: a/b, [int(num) for num in data[:i]])}

while index < len(data):
    if data[index] in '*-+/':
        result = operators[data[index]](index)
        [data.pop(1) for el in range(index)]
        data[0] = result
        index = 0
    index += 1
print(int(data[0]))