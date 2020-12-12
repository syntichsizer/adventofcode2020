def part1(bag, dict, outer_bags = []):
    count = 0
    for k,v in dict.items():
        if k not in outer_bags:
            if bag in v:
                count += 1
                outer_bags.append(k)
                count += part1(k, dict, outer_bags)
    return count

def part2(bag, dict):
    sum = 0
    if bag in dict.keys():
        for k,v in dict[bag].items():
            if v.isnumeric():
                sum += int(v) + (int(v) * part2(k, dict))
            else: return 0
    return sum

bags=[]
bag_dict={}

for line in open(r'input.txt', 'r'):
    line = line[:-1]
    bags.append(line.split())

for bag in bags:
    bag_name = bag[0] + ' ' + bag[1]
    bag_dict[bag_name] = {}

    for index, word in enumerate(bag[3:],3):
        if word[:-1] == 'bag' or word[:-1] == 'bags':
            curr_bag_name = bag[index-2] + ' ' + bag[index-1]
            bag_dict[bag_name][curr_bag_name] = bag[index-3]

x= part1('shiny gold', bag_dict)
y = part2('shiny gold', bag_dict)
print(x, y)
