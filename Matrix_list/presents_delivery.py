num_presents = int(input())
present_gift = 0
size = int(input())
nice_kids = 0

matrix = []
positions = {'up': (-1, 0),
             'down': (1, 0),
             'left': (0, -1),
             'right': (0, 1)}
Santa = []

for n in range(size):
    matrix.append(input().split())
    if 'S' in matrix[n]:
        Santa = [n, matrix[n].index('S')]
        matrix[n][matrix[n].index('S')] = '-'
    if 'V' in matrix[n]:
        nice_kids += matrix[n].count('V')

all_nice_kids = nice_kids

while num_presents > 0:
    command = input()

    row, column = Santa
    if command == 'Christmas morning':
        break

    row += positions[command][0]
    column += positions[command][1]
    if not (0 <= row < size and 0 <= column < size):
        continue

    if matrix[row][column] == 'V':
        present_gift += 1
        num_presents += -1
        matrix[row][column] = '-'
        nice_kids -= 1

    elif matrix[row][column] == 'X':
        matrix[row][column] = '-'

    elif matrix[row][column] == 'C':

        for direction, move in positions.items():
            x = matrix[row+move[0]][column+move[1]]
            if x == 'V':
                num_presents -= 1
                present_gift += 1
                nice_kids -= 1
                matrix[row + move[0]][column + move[1]] = '-'
            elif x == 'X':
                num_presents -= 1
                matrix[row + move[0]][column + move[1]] = '-'

    Santa = [row, column]

matrix[Santa[0]][Santa[1]] = 'S'
if nice_kids:

    print('Santa ran out of presents!')
    [print(' '.join(el)) for el in matrix]
    print(f"No presents for {nice_kids} nice kid/s.")
else:
    [print(' '.join(el)) for el in matrix]
    print(f"Good job, Santa! {all_nice_kids} happy nice kid/s.")






