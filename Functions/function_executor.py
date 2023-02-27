
def func_executor(*args):
    results = []
    for el in args:
        results.append(f'{el[0].__name__} - {el[0](*el[1])}')
    return '\n'.join(results)


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result


def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result


print(func_executor((make_upper, ("Python", "softUni")),(make_lower, ("PyThOn",)),))
