size = int(input())
matrix = []
coordinates = []
directions = {'up': (-1, 0),
             'down': (1, 0),
             'left': (0, -1),
             'right': (0, 1)}
enemy = 3
tenacity = 3
for i in range(size):
    matrix.append([el for el in input()])
    if 'S' in matrix[i]:
        coordinates.append([i, matrix[i].index('S')])
        matrix[i][matrix[i].index('S')] = '-'


while enemy:
    command = input()
    row, column = coordinates[0]
    row += directions[command][0]
    column += directions[command][1]
    if 0 <= row < size and 0 <= column < size:
        coordinates[0] = [row, column]
        if matrix[row][column] == 'C':
            enemy -= 1
            matrix[row][column] = '-'
        elif matrix[row][column] == '*':
            matrix[row][column] = '-'
            tenacity -= 1
            if not tenacity:
                print(f'Mission failed, U-9 disappeared! Last known coordinates {coordinates[0]}!')
                matrix[row][column] = 'S'

                break

else:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
    matrix[coordinates[0][0]][coordinates[0][1]] = 'S'
[print(''.join(n)) for n in matrix]




