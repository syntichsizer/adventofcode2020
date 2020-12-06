from collections import Counter

def everyone(str, n_ppl):
    sum=0
    for v in Counter(str).values():
        if v==n_ppl:
            sum += 1
    return sum

sum = sum_2 = n_ppl = 0
str = ''

for line in open(r'input.txt', 'r'):
    line = line[:-1]
    if len(line) > 0:
        str += line
        n_ppl+=1
    else:
        sum += len(set(str))
        sum_2 += everyone(str, n_ppl)
        str = ''
        n_ppl=0

sum += len(set(str))
sum_2 += everyone(str, n_ppl)

print(sum)

print(sum_2)
