from collections import deque

pizza_orders = deque([int(n) for n in input().split(', ')])
employees_pizza_capacities = [int(n) for n in input().split(', ')]
total_pizza = 0

while pizza_orders and employees_pizza_capacities:
    pizza_nums = pizza_orders.popleft()
    if pizza_nums > 10:
        continue
    if pizza_nums <= 0:
        continue
    employer = employees_pizza_capacities.pop()
    if employer < pizza_nums:
        pizza_orders.appendleft(pizza_nums - employer)
        total_pizza += employer
    else:
        total_pizza += pizza_nums

if pizza_orders:
    print('Not all orders are completed.')
    print(f"Orders left: {', '.join(list(map(str, pizza_orders)))}")
else:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizza}')
    print(f"Employees: {', '.join(list(map(str, employees_pizza_capacities)))}")

