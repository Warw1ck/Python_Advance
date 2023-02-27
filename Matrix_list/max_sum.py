rows, columns = input().split()
matrix = [[int(num) for num in input().split()]for el in range(int(rows))]
counter = 0
max_num = []

for row in range(int(rows) - 2):
    for column in range(int(columns) + 2):
        first_row = matrix[row][column:column+3]
        second_row = matrix[row+1][column:column+3]
        third_row = matrix[row+2][column:column+3]

        if sum(first_row) + sum(second_row) + sum(third_row) > counter:
            max_num = [first_row, second_row, third_row]
            counter = sum(first_row) + sum(second_row) + sum(third_row)
print(f'Sum = {counter}')
[print(*bigest_row) for bigest_row in max_num]
