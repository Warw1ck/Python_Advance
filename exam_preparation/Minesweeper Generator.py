size = int(input())
matrix = [[0]*size for i in range(size)]

bombs_num = int(input())

positions = {'up': (-1, 0),
             'down': (1, 0),
             'left': (0, -1),
             'right': (0, 1),
             'left_up_diagonal': (-1, -1),
             'right_up_diagonal': (-1, +1),
             'left_down_diagonal': (1, -1),
             'right_down_diagonal': (1, +1)
             }

for i in range(bombs_num):
    bomb_coordinates = input()
    bomb_coordinates = bomb_coordinates.replace('(', '')
    bomb_coordinates = bomb_coordinates.replace(')', '')
    row = int(bomb_coordinates.split(', ')[0])
    col = int(bomb_coordinates.split(', ')[1])
    matrix[row][col] = '*'
    for row_value, col_value in positions.values():
        new_row = row + row_value
        new_col = col + col_value
        if 0 <= new_row < size and 0 <= new_col < size:
            if matrix[new_row][new_col] != '*':
                matrix[new_row][new_col] += 1
[print(' '.join(map(str, el)))for el in matrix]


