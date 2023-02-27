size = int(input())
matrix = []
positions = {'up': (-1, 0),
             'down': (1, 0),
             'left': (0, -1),
             'right': (0, 1)}
bunny = []
collecting_position = []
total_eggs = 0
best_direction = ''

for n in range(size):
    matrix.append(input().split())
    if 'B' in matrix[n]:
        bunny = [n, matrix[n].index('B')]

for position, move in positions.items():
    pos_row, pos_colum = [bunny[0] + move[0], bunny[1] + move[1]]
    index_row = []
    index_row.clear()
    eggs = 0
    while 0 <= pos_row < size and 0 <= pos_colum < size:
        if matrix[pos_row][pos_colum] == 'X':
            break

        index_row.append([pos_row, pos_colum])

        eggs += int(matrix[pos_row][pos_colum])
        pos_row += move[0]
        pos_colum += move[1]

        if eggs > total_eggs:
            total_eggs = eggs
            best_direction = position
            collecting_position = index_row

print(best_direction)
print(*collecting_position, sep='\n')
print(total_eggs)

