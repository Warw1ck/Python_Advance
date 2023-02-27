from collections import deque

egg_size = deque(map(int, input().split(', ')))
paper_size = deque(map(int, input().split(', ')))
box_full = 0

while egg_size and paper_size:
    egg = egg_size.popleft()
    paper = paper_size.pop()
    suma = egg + paper
    if egg == 13:
        paper_size.append(paper_size.popleft())
        paper_size.appendleft(paper)
        continue
    elif egg < 1:
        paper_size.append(paper)
    elif suma <= 50:
        box_full += 1

if box_full:
    print(f"Great! You filled {box_full} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if egg_size:
    print(f"Eggs left: {', '.join(list(map(str, egg_size)))}")
if paper_size:
    print(f"Pieces of paper left: {', '.join(list(map(str, paper_size)))}")
