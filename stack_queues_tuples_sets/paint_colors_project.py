data = input().split()
colors_data = {'red', 'yellow', 'blue', 'purple', 'green', 'orange'}
secondary_colors = {'purple': ['red', 'blue'], 'green': ['yellow', 'blue'], 'orange': ['yellow', 'red']}
result = []
while data:

    if len(data) > 1:
        first_color = data.pop(0)
        second_color = data.pop()
    else:
        color = data.pop()
        if color in colors_data:
            result.append(color)
        continue

    if f'{first_color}{second_color}' in colors_data:
        result.append(f'{first_color}{second_color}')
    elif f'{second_color}{first_color}' in colors_data:
        result.append(f'{second_color}{first_color}')

    else:

        if first_color[:len(first_color) - 1]:
            data.insert(int(len(data)/2), first_color[:len(first_color)-1])
        if second_color[:len(second_color) - 1]:
            data.insert(int(len(data)/2), second_color[:len(second_color)-1])

for i in result:
    if i in secondary_colors:
        if secondary_colors[i][0] not in result:
            result.remove(i)
        if secondary_colors[i][1] not in result:
            result.remove(i)

print(result)

