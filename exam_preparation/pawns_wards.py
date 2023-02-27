size = 8
matrix = []

players = {'w': 'White', 'b': 'Black'}
players_position = {'w': [], 'b': []}
column_chars = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}

for i in range(size):
    matrix.append(input().split())
    if 'w' in matrix[i]:
        players_position['w'].append(i)
        players_position['w'].append(matrix[i].index('w'))
    if 'b' in matrix[i]:
        players_position['b'].append(i)
        players_position['b'].append(matrix[i].index('b'))

current_player, next_player = 'w', 'b'

move = 0

while True:
    row, column = players_position[current_player]

    if current_player == 'w':
        move = -1
    if current_player == 'b':
        move = 1

    if column - 1 >= 0:
        if row + move == players_position[next_player][0] and column-1 == players_position[next_player][1]:

            print(f'Game over! {players[current_player]} win, capture on {column_chars[column ]}{8 - players_position[next_player][0]}.')
            break

    if column+1 < size:

        if row + move == players_position[next_player][0] and column + 1 == players_position[next_player][1]:
            print(f'Game over! {players[current_player]} win, capture on {column_chars[column + 2]}{8 - players_position[next_player][0]}.')
            break

    row += move

    if row == 0 and current_player == 'w':
        print(f'Game over! {players[current_player]} pawn is promoted to a queen at {column_chars[column+1]}8.')
        break

    if row == 8 and current_player == 'b':
        print(f'Game over! {players[current_player]} pawn is promoted to a queen at {column_chars[column+1]}1.')
        break

    players_position[current_player] = [row, column]

    current_player, next_player = next_player, current_player
