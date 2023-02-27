matrix = []
my_position = []
shot_targets = []

targets_num = 0
positions = {'up': (-1, 0),
             'down': (1, 0),
             'left': (0, -1),
             'right': (0, 1)}

for n in range(5):
    matrix.append(input().split())
    if 'A' in matrix[n]:
        my_position = [n, matrix[n].index('A')]
        matrix[n][matrix[n].index('A')] = '.'
    if 'x' in matrix[n]:
        targets_num += matrix[n].count('x')

for i in range(int(input())):
    command, *info = input().split()
    row, column = my_position
    if command == 'move':
        for _ in range(int(info[1])):
            row += positions[info[0]][0]
            column += positions[info[0]][1]

        if 0 <= row < 5 and 0 <= column < 5 and matrix[row][column] == ".":
            my_position = [row, column]
    elif command == 'shoot':
        while 0 <= row < 5 and 0 <= column < 5:
            if matrix[row][column] == 'x':
                shot_targets.append([row, column])
                matrix[row][column] = '.'
                break
            row += positions[info[0]][0]
            column += positions[info[0]][1]
    if len(shot_targets) == targets_num:
        print(f"Training completed! All {targets_num} targets hit.")
        print(*shot_targets, sep='\n')
        break
else:
    print(f'Training not completed! {targets_num - len(shot_targets)} targets left.')
    print(*shot_targets, sep='\n')
