elements = set()
data = [input().split() for i in range(int(input()))]
for n in range(len(data)):
    for element in data[n]:
        elements.add(element)

for chemical in elements:
    print(chemical)