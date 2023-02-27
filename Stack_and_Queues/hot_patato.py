data = input().split()
num = int(input())
counter = 0
index = 0
while len(data) > 1:
    counter = 0
    for i in range(len(data)):
        counter += 1
        index += 1
        if index == num:
            print(f'Removed {data.pop(counter-1)}')
            index = 0
            counter -= 1
        if len(data) == 1:
            break
print(f'Last is {data[0]}')


