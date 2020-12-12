# I wanted to solve it without brute force, but couldn't think of anything better. :(

import copy


def boot(lines):
    accumulator = 0
    i = 0
    visited = {}
    length = len(lines)-1

    while True:
        # print(lines[i])
        if i > length:
            return True, accumulator
        elif i in visited.keys():
            return False, accumulator
        else:
            old_i = i
            if lines[i][0] == 'acc':
                accumulator += int(lines[i][1])
            elif lines[i][0] == 'jmp':
                i += int(lines[i][1])

            visited[old_i] = 'loop'
            if old_i == i:
                i += 1


def modify(lines, index):
    lines[index][0] = 'nop' if lines[index][0] == 'jmp' else 'jmp'
    return lines


def part2(lines):
    for index, line in enumerate(lines):
        if line[0] in ['jmp', 'nop']:
            modify(lines, index)
            state, acc = boot(lines)
            modify(lines, index)

            if state:
                return acc


lines = []

for line in open(r'input.txt', 'r'):
    line = line[:-1].split()
    lines.append([line[0], line[1]])

print(boot(lines)[1])

print(part2(lines))
