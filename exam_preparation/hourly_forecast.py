
def forecast(*args):
    sunny_dict = {}
    cloudy_dict = {}
    rainy_dict = {}
    my_print = []

    for el in args:
        if el[1] == 'Sunny':
            sunny_dict[el[0]] = el[1]
        elif el[1] == 'Cloudy':
            cloudy_dict[el[0]] = el[1]
        elif el[1] == 'Rainy':
            rainy_dict[el[0]] = el[1]

    for key, value in sorted(sunny_dict.items()):
        my_print.append(f'{key} - {value}')

    for key, value in sorted(cloudy_dict.items()):
        my_print.append(f'{key} - {value}')

    for key, value in sorted(rainy_dict.items()):
        my_print.append(f'{key} - {value}')

    return '\n'.join(my_print)



print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

