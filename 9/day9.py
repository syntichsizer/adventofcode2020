def find_number(numbers):
    preamble = 25
    for index, sum in enumerate(numbers[preamble:], preamble):
        prev = numbers[index-preamble:index]
        if not [n for n in prev if sum-n in prev]: return sum


def find_weakness(num, numbers):
    for i, first_n in enumerate(numbers):
        lst=[first_n]
        for n in numbers[i+1:]:
            lst.append(n)
            s = sum(lst)
            if s > num: break
            if s == num: return min(lst) +  max(lst)


numbers = []

for line in open(r'input.txt', 'r'):
    line = line[:-1]
    numbers.append(int(line))

n = find_number(numbers)

print(n)

print(find_weakness(n, numbers))
