size = 7
players = input().split(', ')
matrix = [input().split() for i in range(size)]
points = {players[0]: [501, 0], players[1]: [501, 0]}
current_player, next_player = players[0], players[1]
while True:
    coordinates = input()
    coordinates = coordinates.replace('(', '')
    coordinates = coordinates.replace(')', '')
    row, col = coordinates.split(', ')
    row = int(row)
    col = int(col)
    points[current_player][1] += 1

    if 0 <= row < size and 0 <= col < size:
        if matrix[row][col].isdigit():
            points[current_player][0] -= int(matrix[row][col])
        elif matrix[row][col] == 'D':
            points[current_player][0] -= 2 * (int(matrix[0][col]) + int(matrix[size-1][col]) + int(matrix[row][0]) + int(matrix[row][size-1]))
        elif matrix[row][col] == 'T':
            points[current_player][0] -= 3 * (int(matrix[0][col]) + int(matrix[size-1][col]) + int(matrix[row][0]) + int(matrix[row][size-1]))
        elif matrix[row][col] == 'B':
            print(f"{current_player} won the game with {points[current_player][1]} throws!")
            break
        if points[current_player][0] <= 0:
            print(f"{current_player} won the game with {points[current_player][1]} throws!")
            break
    current_player, next_player = next_player, current_player
