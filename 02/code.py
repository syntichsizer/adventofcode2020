def first(list):
    counter = 0

    for line in list:
        first = line.split('-')
        second = first[1].split()

        a = int(first[0])
        b = int(second[0])

        letter = second[1][0]

        str = second[2]

        lcount = str.count(letter)

        if lcount >= a and lcount <= b:
            counter += 1

    return counter

def second(list):
    counter = 0
    for line in list:
        first = line.split('-')
        second = first[1].split()

        a = int(first[0])-1
        b = int(second[0])-1

        letter = second[1][0]

        str = second[2]

        if (str[a] == letter) ^ (str[b] == letter):
            counter += 1

    return counter


list=[]

for line in open(r'input.txt', 'r'):
    list.append(line[:-1])


print(first(list))
print(second(list))
