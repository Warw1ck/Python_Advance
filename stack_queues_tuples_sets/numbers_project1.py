first = set(num for num in input().split())
second = set(num for num in input().split())

commands = {'Add First': lambda x: [first.add(element) for element in x],
            'Add Second': lambda x: [second.add(element) for element in x],
            'Remove First': lambda x: [first.discard(el) for el in x],
            'Remove Second': lambda x: [second.discard(el) for el in x],
            'Check Subset': lambda: True if first.issubset(second) or second.issubset(first) else False}

for i in range(int(input())):
    command, *data = input().split()
    if len(data) > 1:
        commands[f'{command} {data.pop(0)}'](data)
    else:
        print(commands[f'{command} {data.pop(0)}']())

print(', '.join(sorted(first)))
print(', '.join(sorted(second)))
