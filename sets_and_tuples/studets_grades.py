the_class = {}

for i in range(int(input())):
    student = input().split()
    if student[0] not in the_class:
        the_class[student[0]] = [student[1]]
    else:
        the_class[student[0]].append(student[1])

for key, value in the_class.items():
    num_value = [float(n) for n in value]
    print(f"{key} -> {' '.join(map(str, value)):} (avg: {sum(num_value)/len(num_value):.2f})")