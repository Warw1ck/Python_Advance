from _collections import deque

robots_active = deque([n.split('-') for n in input().split(';')])
robots_not_active = []
all_products = deque([])
time_start = input().split(':')
time_pass = 0
new_hour = []
counter = 0
new = ''
counter_products = True

while True:
    time_pass += 1

    for n in time_start:
        counter = 0
        new = ''
        for ch in n:

            counter += 1
            if counter == 1 and ch == '0':
                pass
            else:
                new += ch
        new_hour.append(new)

    new_hour[2] = int(new_hour[2]) + 1
    if int(new_hour[2]) > 59:
        new_hour[2] = int(new_hour[2]) - 60
        new_hour[1] = int(new_hour[1]) + 1

        if int(new_hour[1]) > 59:
            new_hour[1] = int(new_hour[1]) - 60
            new_hour[0] = int(new_hour[0]) + 1
            if int(new_hour[0]) > 23:
                new_hour[0] = 0

    for i in range(len(robots_active)):
        robots_active[i][1] = int(robots_active[i][1])
        robots_active[i][1] += 1

    if counter_products:
        product = input()
        if product != 'End':
            all_products.append(product)

    if product == 'End':
        counter_products = False
        if not all_products:
            break

    if robots_active:
        l = robots_active.popleft()
        robots_not_active.append(l)
        robot,  time = l
        print(f"{robot} - {all_products.popleft()} [{int(new_hour[0]):02d}:{int(new_hour[1]):02d}:{int(new_hour[2]):02d}]")

    else:
        all_products.append(all_products.popleft())

    for i in robots_not_active:
        if i[1] == time_pass:
            robots_active.append(i)





