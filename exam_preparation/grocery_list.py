def shop_from_grocery_list(*args):
    budged, grocery_list, *shop = args
    for item, prise in shop:
        if item in grocery_list:
            if budged >= prise:
                budged -= prise
                grocery_list.remove(item)
    if not grocery_list:
        return f'Shopping is successful. Remaining budget: {budged:.02f}.'
    else:
        return f"You did not buy all the products. Missing products: {''.join(grocery_list)}."



print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

