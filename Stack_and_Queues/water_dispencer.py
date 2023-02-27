from _collections import deque
quantity = int(input())
my_list = deque()
while True:
    names = input()
    if names == 'Start':
        break
    my_list.append(names)
while True:
    command = input()
    command = command.split()
    if command[0] == 'refill':

        quantity += int(command[1])
    elif command[0] == 'End':
        print(f'{quantity} liters left')
        break
    else:
        if int(command[0]) > quantity:
            print(f'{my_list.popleft()} must wait')
        else:
            quantity -= int(command[0])
            print(f'{my_list.popleft()} got water')





