def even_odd_filter(**kwargs):
    if 'even' in kwargs:
        kwargs['even'] = [el for el in kwargs['even'] if el % 2 == 0]
    if 'odd' in kwargs:
        kwargs['odd'] = [el for el in kwargs['odd'] if el % 2 == 1]
    return dict(sorted(kwargs.items()))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],))
