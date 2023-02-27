def add_songs(*args):
    result = {}
    for el in args:
        if f'- {el[0]}' in result:
            if el[1]:
                result[f'- {el[0]}'] += el[1]
        else:
            result[f'- {el[0]}'] = el[1]
            result[f'- {el[0]}'].insert(0, f'- {el[0]}')
    result_print = []
    for value in result.values():
        result_print += value

    return '\n'.join(result_print)





print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))



