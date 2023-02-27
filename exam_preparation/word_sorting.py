def words_sorting(*args):
    word_dict = {}
    suma = 0
    for el in args:
        word_dict[el] = sum([ord(ch)for ch in el])
    for value in word_dict.values():
        suma += value
    if suma % 2 == 0:
        return '\n'.join([f'{key} - {value}' for key, value in sorted(tuple(word_dict.items()), key=lambda x: x[0])])
    else:
        return '\n'.join([f'{key} - {value}' for key, value in sorted(tuple(word_dict.items()), key=lambda x: -x[1])])


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

