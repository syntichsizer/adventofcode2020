# I know it's not the prettiest thing ever but it works and i'm tired. 

def part1(exp):
    def plus(a,b):
        return a+b
    def times(a,b):
        return a*b
    value = 0
    sign = plus
    i=0
    while i < len(exp):
        if exp[i] == '+': sign = plus
        elif exp[i] == '*': sign = times
        elif exp[i] == '(':
            count = 1
            old_i = i
            while count > 0:
                i+=1
                if exp[i] == '(': count += 1
                elif exp[i] == ')': count -= 1
            value = sign(value, part1(exp[old_i+1:i]))
        elif exp[i] == ')': return value
        else: value = sign(value, int(exp[i]))
        i+=1
    return value

def part2(exp):
    exp = list(exp)
    value = 0
    i = 0

    while i < len(exp):
        if exp[i] == '(':
            count = 1
            temp_i = i
            while count > 0:
                temp_i+=1
                if exp[temp_i] == '(': count += 1
                elif exp[temp_i] == ')': count -= 1
            exp[i] = part2(exp[i+1:temp_i])
            del exp[i+1:temp_i+1]
        i+=1

    i=0
    while i < len(exp):
        if exp[i] == '+':
            exp[i] = int(exp[i-1]) + int(exp[i+1])
            exp.pop(i+1)
            exp.pop(i-1)
            i-=1
        i+=1
    i=0
    while i < len(exp):
        if exp[i] == '*':
            exp[i] = int(exp[i-1]) * int(exp[i+1])
            exp.pop(i+1)
            exp.pop(i-1)
            i-=1
        i+=1

    return exp[0]

expressions = [line[:-1].replace(' ', '') for line in open(r'input.txt', 'r')]

sum=0

for exp in expressions:
    sum+=part1(exp)

print(sum)

sum = 0

for exp in expressions:
    sum += part2(exp)

print(sum)
