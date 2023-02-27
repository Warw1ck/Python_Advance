rows = int(input())
matrix = [list(input()) for p in range(rows)]
possible_moves = ((-1, -2), (-1, 2), (1, -2), (1, 2), (-2, 1), (-2, -1), (2, 1), (2, -1))
knight_removed = 0

while True:
    most_attacks = 0
    knight_position = []
    for i in range(rows):
        for j in range(rows):
            if matrix[i][j] == 'K':
                attack = 0
                for move in possible_moves:
                    if not (0 <= i+move[0] < rows and 0 <= j+move[1] < rows):
                        continue
                    if matrix[i+move[0]][j+move[1]] == 'K':
                        attack += 1
                if attack > most_attacks:
                    knight_position = [i, j]
                    most_attacks = attack
    if knight_position:
        matrix[knight_position[0]][knight_position[1]] = 0
        knight_removed +=1
    else:
        break

print(knight_removed)

