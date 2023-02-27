n, m = map(int, input().split())

matrix = []
my_coordinates = []
enemy_touch = 0
moves = 0

for i in range(n):
    matrix.append(input().split())
    if 'B' in matrix[i]:
        my_coordinates = [i, matrix[i].index('B')]
        matrix[i][matrix[i].index('B')] = '-'


positions = {'up': (-1, 0),
             'down': (1, 0),
             'left': (0, -1),
             'right': (0, 1)}

while enemy_touch != 3:
    row, col = my_coordinates

    command = input()
    if command == 'Finish':
        break
    row += positions[command][0]
    col += positions[command][1]
    if 0 <= row < n and 0 <= col < n and matrix[row][col] != 'O':
        if matrix[row][col] == 'P':
            enemy_touch += 1
            matrix[row][col] = '-'
        moves += 1
        my_coordinates = [row, col]

print(f"Game over!\nTouched opponents: {enemy_touch} Moves made: {moves}")
