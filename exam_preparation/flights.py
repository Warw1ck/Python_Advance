def flights(*args):
    destination = {}
    for n in range(0, len(args), 2):
        if args[n] == 'Finish':
            break
        if args[n] not in destination:
            destination[args[n]] = args[n+1]
        else:
            destination[args[n]] += args[n+1]

    return destination







print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))