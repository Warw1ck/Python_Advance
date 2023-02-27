n_length, m_length = input().split()

n = {int(input()) for i in range(int(n_length))}
m = {int(input()) for l in range(int(m_length))}

both_sets = n.intersection(m)

for n in both_sets:
    print(n)
