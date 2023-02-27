rows, columns = input().split()
matrix = [input().split() for el in range(int(rows))]
counter = 0

for row in range(int(rows) - 1):
    for column in range(int(columns) - 1):
        symbol = matrix[row][column]
        if symbol == matrix[row+1][column] and symbol == matrix[row+1][column+1] and symbol == matrix[row][column+1]:
            counter += 1

print(counter)
