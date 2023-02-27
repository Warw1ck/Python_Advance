def shopping_cart(*args):
    result = {'Soup': [], 'Pizza': [], 'Dessert': []}
    for el in args:
        if el == 'Stop':
            break

        key, product = el
        if key == 'Pizza' and len(result['Pizza']) == 4:
            continue
        elif key == 'Soup' and len(result['Soup']) == 3:
            continue
        elif key == 'Dessert' and len(result['Dessert']) == 2:
            continue
        if f' - {product}' not in result[key]:
            result[key].append(f' - {product}')

    if not result['Soup'] and not result['Pizza'] and not result['Dessert']:
        return 'No products in the cart!'
    print_result = []
    for key, value in sorted(tuple(result.items()), key=lambda x: (-len(x[1]), x[0])):
        print_result.append(f"{key}:")
        print_result += sorted(value)

    return '\n'.join(print_result)







print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

