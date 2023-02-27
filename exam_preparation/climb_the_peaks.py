from collections import deque


mountain_peaks = deque([(80, 'Vihren'), (90, 'Kutelo'), (100, 'Banski Suhodol'), (60, 'Polezhan'), (70, 'Kamenitza')])
days = 0
conqueror = []
food_portions = [int(el) for el in input().split(', ')]
stamina = deque([int(el) for el in input().split(', ')])


while mountain_peaks:
    if days == 7 or not food_portions or not stamina:
        print('Alex failed! He has to organize his journey better next time -> @PIRINWINS')
        print('\n'.join(conqueror))
        break

    food_num = food_portions.pop()
    stamina_num = stamina.popleft()
    difficulty, peak = mountain_peaks[0]
    suma = food_num + stamina_num
    if suma >= difficulty:
        mountain_peaks.popleft()
        conqueror.append(peak)
        days += 1
    else:
        days += 1


else:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")

if conqueror:
    print('Conquered peaks:')
    print('\n'.join(conqueror))

