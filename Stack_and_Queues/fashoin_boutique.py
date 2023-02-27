box = list(map(int, input().split(' ')))
rack_num = int(input())
racks = 0
counter = 0
while box:
    l = box[len(box)-1]
    counter += l
    if counter <= rack_num:
        box.pop(len(box)-1)
    if counter >= rack_num:
        racks += 1
        counter = 0

if counter > 0:
    racks += 1
print(racks)



