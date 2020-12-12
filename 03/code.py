def tree_find(trees, slopes=[(3,1)]):

    multi=1

    ln=len(trees[0])

    for slope in slopes:
        x=0
        y=0
        tree_count=0
        
        while y < len(trees)-1:
            x += slope[0]
            y += slope[1]

            if x > ln-1:
                x = x-ln

            if trees[y][x] == '#':
                tree_count += 1
        multi *= tree_count

    return multi

trees = []

for line in open(r'input.txt', 'r'):
    trees.append(line[:-1])

print(tree_find(trees))

multi = tree_find(trees, [(1,1),(3,1),(5,1),(7,1),(1,2)])

print(multi)
