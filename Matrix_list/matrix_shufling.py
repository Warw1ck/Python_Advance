rows, columns = map(int, input().split())
matrix = [input().split() for n in range(rows)]


def check_valid(data_inf):
    if set(data_inf[:2]).issubset(valid_rows) and set(data_inf[2:]).issubset(valid_columns):
        return True
    else:
        return False


def swap(data_inf):
    matrix[data_inf[0]][data_inf[1]], matrix[data_inf[2]][data_inf[3]] = matrix[data_inf[2]][data_inf[3]], matrix[data_inf[0]][data_inf[1]]


while True:
    command, *info = [int(x) if x.isdigit() else x for x in input().split()]
    if command == 'END':
        break
    valid_rows = range(rows)
    valid_columns = range(columns)
    if command == 'swap':
        if check_valid(info):
            swap(info)
            [print(' '.join(el)) for el in matrix]
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
