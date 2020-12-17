def memory(list, n):

    dict = {e: i for i, e in enumerate(list[:-1])}
    last = list[-1]

    for i in range(len(list)-1, n):
        lwi = last
        last = i - dict[last] if last in dict.keys() else 0
        dict[lwi] = i

    return lwi

mem=[2,20,0,4,1,17]

print(memory(mem, 2020))
print(memory(mem, 30000000))
