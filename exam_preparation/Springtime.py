def start_spring(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if value not in result:
            result[value] = []
        result[value].append(key)
    the_print = []

    for key, value in sorted(tuple(result.items()), key=lambda x: (-len(x[1]), x[0])):
        the_print.append(f'{key}:')
        [the_print.append(f'-{el}') for el in sorted(value)]
    return '\n'.join(the_print)


example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))

