matrix = [el.split() for el in input().split('|')]
matrix.reverse()
reverce_list = []
for element in matrix:
    x = element
    for _ in range(len(x)):
        reverce_list.append(x.pop(0))

print(*reverce_list)