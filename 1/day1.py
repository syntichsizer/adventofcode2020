def find(list):
    for e in list:
        if 2020-e in list:
            return (2020-e)*e

def find2(list):
    for i, e in enumerate(list):
        for e2 in list[i+1:]:
            if 2020-e-e2 in list:
                return (2020-e-e2)*e*e2

list = []
for line in open(r'input.txt', 'r'):
    list.append(int(line[:-1]))

number=find(list)
print(number)

number=find2(list)
print(number)
