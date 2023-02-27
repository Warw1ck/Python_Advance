numbers = tuple(map(float, input().split()))
count_num = {num: numbers.count(num) for num in numbers}

for key, value in count_num.items():
    print(f'{key} - {value} times')