from collections import deque

bombs_effects = deque([int(n) for n in input().split(', ')])
bombs_casings = deque([int(n) for n in input().split(', ')])
bombs_total = {"Cherry Bombs": 0,
               "Datura Bombs": 0,
               "Smoke Decoy Bombs": 0}
bombs_num = {60: "Cherry Bombs", 40: "Datura Bombs", 120: "Smoke Decoy Bombs"}


while bombs_effects and bombs_casings:
    effect = bombs_effects.popleft()
    casing = bombs_casings.pop()
    suma = effect + casing
    if suma in bombs_num:
        bombs_total[bombs_num[suma]] += 1
    else:
        bombs_effects.appendleft(effect)
        bombs_casings.append(casing-5)
    if bombs_total["Datura Bombs"] > 2 and bombs_total["Cherry Bombs"] > 2 and bombs_total["Smoke Decoy Bombs"] > 2:
        print("Bene! You have successfully filled the bomb pouch!")
        break
else:
    print("You don't have enough materials to fill the bomb pouch.")

print(f"Bomb Effects: {', '.join([str(el) for el in bombs_effects]) if bombs_effects else 'empty'}")
print(f"Bomb Casings: {', '.join([str(el) for el in bombs_casings]) if bombs_casings else 'empty'}")
for key, value in bombs_total.items():
    print(f'{key}: {value}')




