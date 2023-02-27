size = int(input())
matrix = []
alice = []
total_tea = 0

for n in range(size):
    matrix.append(input().split())
    if 'A' in matrix[n]:
        alice = [n, matrix[n].index('A')]
        matrix[n][matrix[n].index('A')] = '*'


while True:
    command = input()
    row, column = alice

    if command == 'up':
        row += -1
    elif command == 'down':
        row += 1
    elif command == 'left':
        column += -1
    elif command == 'right':
        column += 1

    if not (0 <= row < size and 0 <= column < size):
        print("Alice didn't make it to the tea party.")
        break
    if matrix[row][column] == 'R':
        matrix[row][column] = '*'
        print("Alice didn't make it to the tea party.")
        break

    if matrix[row][column].isdigit():
        total_tea += int(matrix[row][column])
        if total_tea >= 10:
            matrix[row][column] = '*'
            print('She did it! She went to the party.')
            break
    matrix[row][column] = '*'
    alice = [row, column]
[print(*el) for el in matrix]

