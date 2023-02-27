from collections import deque
materials = deque([int(num) for num in input().split()])
magic_total = deque([int(num) for num in input().split()])
toys_prise = {150: 'Doll',
              250: 'Wooden train',
              300: 'Teddy bear',
              400: 'Bicycle'}
toys_crafted = {}
money = 0

while materials and magic_total:
    material = materials.pop() if magic_total[0] or not materials[0] else 0
    magic = magic_total.popleft() if material or not magic_total[0] else 0
    if not magic:
        continue

    money = material * magic

    if money in toys_prise:
        if toys_prise[money] not in toys_crafted:
            toys_crafted[toys_prise[money]] = 0
        toys_crafted[toys_prise[money]] += 1
    elif money < 0:
        materials.append(material+magic)
        continue
    elif money > 0:
        materials.append(material+15)

if {'Doll', 'Wooden train'}.issubset(toys_crafted) or {'Bicycle', 'Teddy bear'}.issubset(toys_crafted):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials:
    materials.reverse()
    print(f"Materials left: {', '.join(map(str,materials))}")

if magic_total:
    print(f"Magic left: {', '.join(map(str,magic_total))}")

for key, value in sorted(toys_crafted.items()):
    print(f'{key}: {value}')
