size = int(input())
matrix = []
snake = []
burrows = []
food_eaten = 0

positions = {'up': (-1, 0),
             'down': (1, 0),
             'left': (0, -1),
             'right': (0, 1)}

for i in range(size):
    matrix.append([ch for ch in input()])
    for n in range(len(matrix[i])):
        if 'S' == matrix[i][n]:
            snake = [i, n]
            matrix[i][n] = '.'
        if 'B' == matrix[i][n]:
            burrows.append([i, n])

if burrows:
    first_burrow, second_burrow = burrows

while True:
    command = input()
    row, col = snake
    row += positions[command][0]
    col += positions[command][1]

    if 0 <= row < size and 0 <= col < size:

        if matrix[row][col] == 'B':
            if [row, col] == first_burrow:
                matrix[row][col] = '.'
                row, col = second_burrow
            else:
                matrix[row][col] = '.'
                row, col = first_burrow
        if matrix[row][col] == '*':
            food_eaten += 1
            if food_eaten == 10:
                matrix[row][col] = 'S'
                print(f"You won! You fed the snake.\nFood eaten: {food_eaten}")
                break

        matrix[row][col] = '.'
        snake = [row, col]

    else:

        print(f"Game over!\nFood eaten: {food_eaten}")
        break


[print(''.join(row_n))for row_n in matrix]

