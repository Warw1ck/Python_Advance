from collections import deque

chocolate = deque([int(num) for num in input().split(', ')])
milk = deque([int(num) for num in input().split(', ')])
milkshake = 0

while milkshake != 5 and chocolate and milk:
    c = chocolate.pop()
    m = milk.popleft()

    if c <= 0 and m <= 0:
        continue

    if c <= 0:
        milk.appendleft(m)
        continue

    if m <= 0:
        chocolate.append(c)
        continue

    if c != m:
        milk.append(m)
        chocolate.append(c-5)

    else:
        milkshake += 1

if milkshake < 5:
    print('Not enough milkshakes.')
else:
    print("Great! You made all the chocolate milkshakes needed!")

print(f"Chocolate: {', '.join(map(str, chocolate)) or 'empty'}")
print(f"Milk: {', '.join(map(str, milk)) or 'empty'}")
