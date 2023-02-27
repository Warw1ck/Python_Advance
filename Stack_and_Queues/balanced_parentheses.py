from _collections import deque


data = deque([ch for ch in input()])
open_parentheses = []

while data:
    x = data.popleft()

    if x in '([{':
        open_parentheses.append(x)
    elif not open_parentheses:
        print('NO')
        break
    else:
        if f'{open_parentheses.pop()}{x}' not in '()[]{}':
            print('NO')
            break
else:
    print('YES')





