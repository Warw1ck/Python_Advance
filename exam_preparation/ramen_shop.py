from collections import deque

ramen_bowls = deque(map(int, input().split(', ')))
customers_num = deque(map(int, input().split(', ')))

while True:
    if not customers_num:
        print("Great job! You served all the customers.")
        break
    elif not ramen_bowls:
        print("Out of ramen! You didn't manage to serve all customers.")
        break

    bowl = ramen_bowls.pop()
    customer = customers_num.popleft()
    if bowl == customer:
        continue
    elif bowl > customer:
        bowl -= customer
        ramen_bowls.append(bowl)
    else:
        customer -= bowl
        customers_num.appendleft(customer)

if ramen_bowls:
    print(f"Bowls of ramen left: {', '.join(list(map(str, ramen_bowls)))}")
elif customers_num:
    print(f"Customers left: {', '.join(list(map(str, customers_num)))}")