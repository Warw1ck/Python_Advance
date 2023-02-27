from collections import deque

elf_energy = deque(map(int, input().split()))
num_materials = deque(map(int, input().split()))
toys_total = 0
energy_total = 0
counter = 0

while elf_energy and num_materials:
    energy = elf_energy.popleft()
    material = num_materials.pop()
    counter += 1
    energy_spend = 0
    toys_made = 0
    energy_left = 0

    if energy < 5:
        num_materials.append(material)
        counter -= 1
        continue

    elif counter % 3 == 0:
        if energy >= material*2:
            energy_left = energy - material*2
            toys_made += 2
            energy_spend += energy - energy_left
            if counter % 5 != 0:
                toys_total += toys_made
                elf_energy.append(energy_left + 1)
            else:
                elf_energy.append(energy_left)

        else:
            elf_energy.append(energy * 2)
            num_materials.append(material)

    elif energy >= material:
        energy_left = energy - material
        toys_made += 1
        energy_spend += energy - energy_left
        if counter % 5 != 0:
            toys_total += toys_made
            elf_energy.append(energy_left + 1)
        else:
            elf_energy.append(energy_left)

    else:
        elf_energy.append(energy*2)
        num_materials.append(material)

    energy_total += energy_spend

print(f'Toys: {toys_total}')
print(f'Energy: {energy_total}')
if elf_energy:
    print(f"Elves left: {', '.join(list(map(str, elf_energy)))}")

else:
    print(f"Boxes left: {', '.join(list(map(str, num_materials)))}")








