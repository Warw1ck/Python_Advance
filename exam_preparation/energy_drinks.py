from collections import deque

num_caffeine = list(map(int, input().split(', ')))
num_drinks = deque(map(int, input().split(', ')))

total_caffeine = 0

while num_caffeine and num_drinks:
    caffeine = num_caffeine.pop()
    drink = num_drinks.popleft()
    dose_caffeine = caffeine*drink
    if dose_caffeine + total_caffeine <= 300:
        total_caffeine += dose_caffeine
    else:
        num_drinks.append(drink)
        if total_caffeine > 30:
            total_caffeine -= 30

if num_drinks:
    print(f"Drinks left: {', '.join(list(map(str, num_drinks)))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")
