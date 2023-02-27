data = {}

for i in range(int(input())):
    my_list = input().split('-')
    n, m = my_list
    first_start, first_end = n.split(',')
    second_start, second_end = m.split(',')

    n_list = {n for n in range(int(first_start), int(first_end)+1)}
    m_list = {l for l in range(int(second_start), int(second_end)+1)}

    diff = n_list.intersection(m_list)
    diff_list = [element for element in diff]
    data[len(diff_list)] = diff_list

print(f"Longest intersection is {data[sorted(data)[-1]]} with length {sorted(data)[-1]}")