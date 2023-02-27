size = int(input())
racing_number = input()
matrix = []
tunnel_coordinates = []
car_coordinates = [[0, 0]]
kilometres = 0

positions = {'up': (-1, 0),
             'down': (1, 0),
             'left': (0, -1),
             'right': (0, 1)}

for i in range(size):
    matrix.append(input().split())
    if 'T' in matrix[i]:
        tunnel_coordinates.append([i, matrix[i].index('T')])
first_tunel, second_tunel = tunnel_coordinates

while True:
    command = input()

    if command == 'End':
        matrix[car_coordinates[0][0]][car_coordinates[0][1]] = 'C'
        print(f"Racing car {racing_number} DNF.")
        break

    row, column = car_coordinates[0]
    row += positions[command][0]
    column += positions[command][1]
    kilometres += 10

    if matrix[row][column] == 'T':
        kilometres += 20
        if [row, column] == first_tunel:
            row = second_tunel[0]
            column = second_tunel[1]
        elif [row, column] == second_tunel:
            row = first_tunel[0]
            column = first_tunel[1]
        matrix[first_tunel[0]][first_tunel[1]] = "."
        matrix[second_tunel[0]][second_tunel[1]] = "."

    elif matrix[row][column] == 'F':
        print(f"Racing car {racing_number} finished the stage!")
        matrix[row][column] = 'C'
        break
    car_coordinates[0] = [row, column]

print(f"Distance covered {kilometres} km.")
[print(''.join(el)) for el in matrix]






