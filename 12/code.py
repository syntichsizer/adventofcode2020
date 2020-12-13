def part1(instructions):
    dir = 90
    dis={0:0, 90:0, 180:0, 270:0}

    for ins in instructions:
        c, num = ins[:1], int(ins[1:])

        if c in ('L', 'R'):
            if c == 'R': dir += num
            elif c == 'L': dir -= num

            if dir >= 360: dir -= 360
            if dir < 0: dir = 360 + dir
        else:
            if c == 'F': temp_dir = dir
            elif c == 'N': temp_dir = 0
            elif c == 'S': temp_dir = 180
            elif c == 'E': temp_dir = 90
            elif c == 'W': temp_dir = 270

            dis[temp_dir] += num


    return abs(dis[0] - dis[180]) + abs(dis[90]-dis[270])

def part2(instructions):

    way = {'n':1, 'e':10, 's':0, 'w':0}
    n_dist=0
    e_dist=0

    for ins in instructions:
        c, num = ins[:1], int(ins[1:])
        if c in ('N', 'S', 'E', 'W'): way[c.lower()] += num
        elif c == 'F':
            n_dist += num * (way['n']-way['s'])
            e_dist += num * (way['e']-way['w'])
        elif c == 'R':
            for _ in range(num//90):
                way['n'], way['e'], way['s'], way['w'] = way['w'], way['n'], way['e'], way['s']
        elif c == 'L':
            for _ in range(num//90):
                way['n'], way['e'], way['s'], way['w'] = way['e'], way['s'], way['w'], way['n']

    return abs(n_dist) + abs(e_dist)

instructions = [line[:-1] for line in open(r'input.txt', 'r')]

print(part1(instructions))
print(part2(instructions))
