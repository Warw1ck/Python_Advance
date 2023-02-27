from collections import deque
counter = 0
quantity = int(input())
sequence = input().split(' ')
left_sequence = deque(sequence)
print(max(map(int, sequence)))
for i in sequence:
    counter += int(i)
    if quantity >= counter:
        left_sequence.popleft()
if left_sequence:
    print(f"Orders left: {' '.join(left_sequence)}")
else:
    print(f"Orders complete")