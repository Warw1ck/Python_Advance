from _collections import deque

my_list = deque()
petrol_left = 0
index = 0


for _ in range(int(input())):
    my_list.append([int(num) for num in input().split()])


new_list = my_list.copy()

while new_list:

    petrol, distance = new_list.popleft()
    petrol_left += petrol
    diff = petrol_left - distance

    if diff < 0:
        index += 1
        my_list.append(my_list.popleft())
        new_list = my_list.copy()
        petrol_left = 0

    else:
        petrol_left -= distance

print(index)