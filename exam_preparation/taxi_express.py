from collections import deque

list_customers = deque([int(n) for n in input().split(', ')])
list_taxis = deque([int(n) for n in input().split(', ')])

total_time = 0

while list_customers:
    if not list_taxis:
        print(f"Not all customers were driven to their destinations\nCustomers left: {', '.join(list(map(str, list_customers)))}")
        break
    customer_time_needed = list_customers.popleft()
    taxi_time = list_taxis.pop()
    if taxi_time >= customer_time_needed:
        total_time += customer_time_needed
    else:
        list_customers.appendleft(customer_time_needed)
else:
    print(f'All customers were driven to their destinations\nTotal time: {total_time} minutes')
    