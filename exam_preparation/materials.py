from collections import deque

all_materials = [int(n) for n in input().split()]
magic_lv_value = deque([int(n) for n in input().split()])
items = {'Gemstone': 0, 'Porcelain Sculpture': 0, 'Gold': 0, 'Diamond Jewellery': 0}
items_names = ['Gemstone', 'Porcelain Sculpture', 'Gold', 'Diamond Jewellery']
succeeded = False

while all_materials and magic_lv_value:
    material = all_materials.pop()
    value = magic_lv_value.popleft()
    magic = material + value
    if magic < 100:
        if magic % 2 == 0:
            magic = material*2 + value*3
        elif magic % 2 == 1:
            magic *= 2
    elif magic > 499:
        magic /= 2

    if 0 < (magic // 100) < 5:
        items[items_names[int((magic // 100)-1)]] += 1

    if items['Gemstone'] and items['Porcelain Sculpture']:
        succeeded = True
    elif items['Gold'] and items['Diamond Jewellery']:
        succeeded = True
if succeeded:
    print('The wedding presents are made!')
else:
    print("Aladdin does not have enough wedding presents.")
if magic_lv_value:
    print(f"Magic left: {', '.join(list(map(str, magic_lv_value)))}")
else:
    print(f"Materials left: {', '.join(list(map(str, all_materials)))}")
for key, value in sorted(items.items()):
    if value:
        print(f"{key}: {value}")


