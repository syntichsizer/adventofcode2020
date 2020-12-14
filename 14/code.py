import itertools
import copy

def v1(instructions):
    memory={}
    for ins in instructions:
        if ins[0] != 'mask':
            ins[0] = int(ins[0][4:-1])
            ins[1] = bin(int(ins[1]))[2:]
            ins[1] = (36 - len(ins[1])) * '0' + ins[1]
            num = int(''.join([c if c!='X' else ins[1][i] for i, c in enumerate(mask)]), 2)
            memory[ins[0]] = num
        else:
            mask = ins[1]



def v2(instuctions):
    memory={}
    for ins in instructions:
        if ins[0] != 'mask':
            ins[0] = bin(int(ins[0][4:-1]))[2:]
            ins[0] = (36 - len(ins[0])) * '0' + ins[0]

            num = [c if c!='0' else ins[0][i] for i, c in enumerate(mask)]
            lst = [i for i, c in enumerate(num) if c == 'X']

            for combination in combinations:
                for i, c in enumerate(combination):
                    num[lst[i]] = str(c)
                memory[int(''.join(num),2)] = int(ins[1])
        else:
            mask = ins[1]
            combinations = list(itertools.product([0, 1], repeat=mask.count('X')))

    return sum([value for value in memory.values()])

instructions = [line[:-1].replace(' ', '').split('=') for line in open(r'input.txt', 'r')]


#print(v1(instructions))
print(v2(instructions))
