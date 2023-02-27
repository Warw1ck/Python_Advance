rows = int(input())
matrix = [input().split(', ') for el in range(int(rows))]
first_diagonal = []
second_diagonal = []

for i in range(len(matrix)):
    first_diagonal.append(matrix[i][i])

for i in range(len(matrix)):
    second_diagonal.append(matrix[i][(len(matrix)-1)-i])

print(f"Primary diagonal: {', '.join(first_diagonal)}. Sum: {sum(map(int,first_diagonal))}")
print(f"Secondary diagonal: {', '.join(second_diagonal)}. Sum: {sum(map(int,second_diagonal))}")

