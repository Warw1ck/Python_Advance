from collections import deque

textiles = deque([int(n) for n in input().split()])
medicaments = deque([int(n) for n in input().split()])


items_total = {'Patch': 0,
               'Bandage': 0,
               'MedKit': 0}

items = {30: 'Patch',
         40: 'Bandage',
         100: 'MedKit'}


while textiles and medicaments:
    first_textile = textiles.popleft()
    last_medicament = medicaments.pop()
    suma = first_textile + last_medicament
    if suma in items:
        items_total[items[suma]] += 1
    elif suma > 100:
        items_total['MedKit'] += 1
        medicaments.append(medicaments.pop() + (suma - 100))
    else:
        medicaments.append(last_medicament+10)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

for key, value in sorted(tuple(items_total.items()), key=lambda x: (-x[1], x[0])):
    if value:
        print(f'{key} - {value}')

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(list(map(str, medicaments)))}")
if textiles:
    print(f"Textiles left: {', '.join(list(map(str, textiles)))}")