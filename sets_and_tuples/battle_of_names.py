set_odd = set()
set_even = set()
for i in range(int(input())):
    name = input()
    value = 0
    for ch in name:
        value += ord(ch)
    value /= (i+1)
    if value % 2 == 1:
        set_odd.add(int(value))
    else:
        set_even.add(int(value))

if sum(set_odd) == sum(set_even):
    union = set_odd.union(set_even)

elif sum(set_odd) > sum(set_even):
    union = set_odd.difference(set_even)

else:
    union = set_odd.symmetric_difference(set_even)

print(', '.join(map(str, union)))
