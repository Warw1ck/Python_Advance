rows = int(input())
matrix = [[int(n) for n in input().split()] for el in range(rows)]
valid = range(rows)
while True:
    command, *info = [x for x in input().split()]
    info = [int(i) for i in info]
    if command == 'END':
        [print(' '.join(map(str, element)))for element in matrix]
        break
    if not(0 <= info[0] < rows and 0 <= info[1] < rows):
        print("Invalid coordinates")
        continue
    if command == 'Add':
        matrix[info[0]][info[1]] += info[2]
    elif command == 'Subtract':
        matrix[info[0]][info[1]] -= info[2]


