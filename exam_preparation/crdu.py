size = 6

matrix = [input().split() for i in range(size)]
coordinates = []
for el in input().split(', '):
    for ch in el:
        if ch not in '()':
            coordinates.append(int(ch))

positions = {'up': (-1, 0),
             'down': (1, 0),
             'left': (0, -1),
             'right': (0, 1)}

while True:
    command, *info = input().split(', ')
    if command == 'Stop':
        [print(' '.join(n))for n in matrix]
        break
    row = coordinates[0]
    column = coordinates[1]
    if command == 'Create':
        row += positions[info[0]][0]
        column += positions[info[0]][1]
        if matrix[row][column] == '.':
            matrix[row][column] = info[1]
    elif command == 'Update':
        row += positions[info[0]][0]
        column += positions[info[0]][1]
        if matrix[row][column] != '.':
            matrix[row][column] = info[1]
    elif command == 'Delete':
        row += positions[info[0]][0]
        column += positions[info[0]][1]
        if matrix[row][column] != '.':
            matrix[row][column] = '.'
    elif command == 'Read':
        row += positions[info[0]][0]
        column += positions[info[0]][1]
        if matrix[row][column] != '.':
            print(matrix[row][column])
    coordinates[0] = row
    coordinates[1] = column



