def grocery_store(**kwargs):
    result = []
    for key, value in sorted(kwargs.items(), key=lambda x: (x[0], -len(x[0]), x[1]), reverse=True):
        result.append(f'{key}: {value}')
    return '\n'.join(result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

