from collections import deque

size = 6
matrix = []

positions = {'up': (-1, 0),
             'down': (1, 0),
             'left': (0, -1),
             'right': (0, 1)}
deposit_check = ['W', 'M', 'C']
deposit = {'W': 'Water deposit ',
           'M': 'Metal deposit ',
           'C': 'Concrete deposit '}

rover = []

for i in range(size):
    matrix.append(input().split())
    if 'E' in matrix[i]:
        rover.append([i, matrix[i].index('E')])

moves = deque(input().split(', '))

while moves:
    move = moves.popleft()
    row, column = rover[0]
    row += positions[move][0]
    column += positions[move][1]
    if 0 > row:
        row = 5
    elif size == row:
        row = 0
    if 0 > column:
        column = 5
    elif size == column:
        column = 0

    place = matrix[row][column]

    if place in deposit:
        print(f'{deposit[place]}found at ({row}, {column})')
        if place in deposit_check:
            deposit_check.remove(place)
    elif place == 'R':
        print(f"Rover got broken at ({row}, {column})")
        break
    rover[0] = [row, column]

if not deposit_check:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")





