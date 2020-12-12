def differences(adapters):
    dict={1:0, 3:0}
    dict[adapters[0]] += 1
    for index, adapter in enumerate(adapters[1:], 1):
            dict[1 if adapter - adapters[index-1] == 1 else 3] += 1
    dict[3] += 1
    return dict[1]*dict[3]


# Tried using recursions for part 2. It worked on
# smaller inputs, but it would take way to long for real puzzle input.
# Then I found a hint on Reddit about Tribonacci sequence and decited
# to solve the puzzle with it. 

# def combinations(adapters, index=0, lst = []):
#     comb = 1
#     point = 0
#
#     if index < len(adapters):
#         adapter = adapters[index]
#         lst.append(adapter)
#
#         if adapter == max(adapters):
#             lst.append('*')
#             #print(lst)
#
#         print(adapter)
#
#         if adapter + 1 in adapters:
#             combinations(adapters, adapters.index(adapter+1), lst)
#             point += 1
#         if adapter + 2 in adapters:
#             combinations(adapters, adapters.index(adapter+2), lst)
#             point +=1
#         if adapter + 3 in adapters:
#             combinations(adapters, adapters.index(adapter+3), lst)
#             point +=1
#
#     return lst

def combinations(adapter):
    comb = {}
    comb[0] = 1
    for adapter in adapters:
        comb[adapter] = comb.get(adapter - 1, 0) + comb.get(adapter - 2, 0) + comb.get(adapter - 3, 0)
    return comb[adapters[-1]]


adapters = [int(line[:-1]) for line in open(r'input.txt', 'r')]

adapters.sort()

print(differences(adapters))
print(combinations(adapters))
