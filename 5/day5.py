from math import floor, ceil

def find_my_id(id_list):
    for id in id_list:
        if id+1 not in id_list and id+2 in id_list:
            return id+1

passes=[]

for line in open(r'input.txt', 'r'):
    passes.append(line[:-1])

max = 0
id_list = []

for p in passes:
    low = 0
    high = 127
    low_s = 0
    high_s = 7

    for letter in p[:-3]:
        if letter == 'F':
            mid = floor((low + high) / 2)
            high = mid
        elif letter == 'B':
            mid = ceil((low + high) / 2)
            low = mid

    for letter in p[-3:]:
        if letter == 'L':
            mid_s = floor((low_s + high_s) / 2)
            high_s = mid_s
        elif letter == 'R':
            mid_s = ceil((low_s + high_s) / 2)
            low_s = mid_s

    id = mid*8 + mid_s;
    id_list.append(id)
    if id>max:
        max=id

print(max)
print(find_my_id(id_list))
