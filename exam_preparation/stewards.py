from collections import deque

seats = input().split(', ')
first_nums = deque(map(int, input().split(', ')))
second_nums = deque(map(int, input().split(', ')))
result = []
rotation = 0

while len(result) < 3 and rotation < 10:
    num1 = first_nums.popleft()
    num2 = second_nums.pop()
    sum = num1 + num2
    rotation += 1
    if f'{num1}{chr(sum)}' in seats:
        seats.remove(f'{num1}{chr(sum)}')
        result.append(f'{num1}{chr(sum)}')
    elif f'{num2}{chr(sum)}' in seats:
        seats.remove(f'{num2}{chr(sum)}')
        result.append(f'{num2}{chr(sum)}')

    else:
        first_nums.append(num1)
        second_nums.appendleft(num2)

print(f"Seat matches: {', '.join(result)}")
print(f'Rotations count: {rotation}')



