data = input()
index = []
for i in range(len(data)):
    char = data[i]
    if char == '(':
        index.append(i)
    elif char == ')':
        l = index.pop()
        print(data[l:i+1])







