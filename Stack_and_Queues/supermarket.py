from _collections import deque
my_list = deque()
COMMAND_PAID = 'Paid'
COMMAND_END = 'End'

while True:
    command = input()
    if command == 'End':
        print(f'{len(my_list)} people remaining.')
        break
    elif command == 'Paid':
        while my_list:
            print(my_list.popleft())
    else:
        my_list.append(command)
