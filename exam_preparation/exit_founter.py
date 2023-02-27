first_player, second_player = input().split(', ')
size = 6
turn = first_player
matrix = [input().split() for i in range(size)]
WALL = False
WALL_HIT_PLAYER = []

while True:

    coordinates = []
    for el in input().split(', '):
        for ch in el:
            if ch not in '()':
                coordinates.append(int(ch))
    if turn in WALL_HIT_PLAYER:
        if turn == first_player:
            turn = second_player
        else:
            turn = first_player
        WALL_HIT_PLAYER.pop(0)
        continue
    row = coordinates[0]
    column = coordinates[1]
    if matrix[row][column] == 'E':
        print(f"{turn} found the Exit and wins the game!")
        break
    elif matrix[row][column] == 'T':
        if turn == first_player:
            print(f"{turn} is out of the game! The winner is {second_player}.")
        else:
            print(f"{turn} is out of the game! The winner is {first_player}.")
        break
    elif matrix[row][column] == 'W':
        print(f'{turn} hits a wall and needs to rest.')
        WALL_HIT_PLAYER.append(turn)
    if turn == first_player:
        turn = second_player
    else:
        turn = first_player


