def concatenate(*args, **kwargs):
    args = ''.join(args)
    index = 0
    for key in kwargs:
        args = args.replace(key, kwargs[key])
    return args


print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))