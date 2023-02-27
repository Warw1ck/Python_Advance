row_m, col_m = list(map(int, input().split(', ')))
matrix = []
items = {'Christmas decorations': 0, 'Gifts': 0, 'Cookies': 0}
positions = {'up': (-1, 0),
             'down': (1, 0),
             'left': (0, -1),
             'right': (0, 1)}
items_number = 0
santa = []
for i in range(row_m):
    matrix.append(input().split())
    if 'Y' in matrix[i]:
        santa.append([i, matrix[i].index('Y')])
        matrix[i][matrix[i].index('Y')] = 'x'
    items_number += matrix[i].count('D')
    items_number += matrix[i].count('G')
    items_number += matrix[i].count('C')


while items_number:
    command = input()

    if command == 'End':
        break

    row, col = santa[0]
    move, steps = command.split('-')

    for _ in range(int(steps)):
        row += positions[move][0]
        col += positions[move][1]

        if 0 > row:
            row = row_m-1
        elif row == row_m:
            row = 0
        if 0 > col:
            col = col_m-1
        elif col == col_m:
            col = 0

        if matrix[row][col] == 'D':
            items['Christmas decorations'] += 1
            items_number -= 1
        elif matrix[row][col] == 'G':
            items_number -= 1
            items['Gifts'] += 1
        elif matrix[row][col] == 'C':
            items['Cookies'] += 1
            items_number -= 1
        if not items_number:
            break
        matrix[row][col] = 'x'
    santa[0] = [row, col]


if not items_number:
    print('Merry Christmas!')
matrix[santa[0][0]][santa[0][1]] = 'Y'
print("You've collected:")
for key, value in items.items():
    print(f'- {value} {key}')
for el in matrix:
    print(' '.join(el))


