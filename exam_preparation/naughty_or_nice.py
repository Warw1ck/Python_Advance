def naughty_or_nice_list(the_kids, *args, **kwargs):
    result = {'Nice': [], 'Naughty': [], 'Not found': []}
    kids = {}
    print_result = []
    numbers = []
    for el in the_kids:
        if el[0] in kids:
            del kids[el[0]]
        else:
            kids[el[0]] = el[1]
    for el in args:
        number, the_list = el.split('-')
        numbers += number
        for kid_number, names in kids.items():
            if kid_number == int(number):

                result[the_list].append(names)
    for kid_number, names in kids.items():
        if f'{kid_number}' not in numbers and names not in kwargs:
            result['Not found'].append(names)
    if kwargs:
        for key, value in kwargs.items():
            if key not in result['Nice'] and key not in result['Naughty']:
                result[value].append(key)

    for key, value in result.items():
        if value:
            print_result.append(f"{key}: {', '.join(value)}")

    return '\n'.join(print_result)


print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))





