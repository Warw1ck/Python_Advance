from collections import deque
bees = deque([int(el) for el in input().split()])
nectar = deque([int(el) for el in input().split()])
symbols = deque([el for el in input().split()])

commands = {'*': lambda a, s: a*s,
            '+': lambda a, s: a+s,
            '-': lambda a, s: a-s,
            '/': lambda a, s: a/s,
            }

total_honey = 0
while bees and nectar:
    b = bees.popleft()
    n = nectar.pop()
    if b > n:
        bees.appendleft(b)
    if b < n:
        total_honey += abs(commands[symbols.popleft()](b, n))

print(f'Total honey made: {total_honey}')
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")