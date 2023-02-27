from collections import deque

flowers = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}

vowels = deque(input().split())
consonants = input().split()

while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for key, value in flowers.items():

        if vowel in flowers[key]:
            flowers[key] = flowers[key].replace(vowel, '', flowers[key].count(vowel))

        if consonant in flowers[key]:
            flowers[key] = flowers[key].replace(consonant, '', flowers[key].count(consonant))

        if not flowers[key]:
            print(f'Word found: {key}')
            if vowels:
                print(f"Vowels left: {' '.join(vowels)}")
            if consonants:
                print(f"Consonants left: {' '.join(consonants)}")
            exit()
else:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")






