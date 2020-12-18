import re
from collections import defaultdict

def invalid(tickets, dict):
    def isValid(value, values):
        for rule in values:
            if (value >= int(rule[0]) and value <= int(rule[1])) or (value >= int(rule[2]) and value <= int(rule[3])):
                return True
        return False
    sum = 0
    new_tickets= []
    for ticket in tickets:
        count = 0
        for value in ticket:
            value = int(value)
            if not isValid(value, dict.values()):
                sum += value
                break
            else: count += 1
        if count == len(ticket): new_tickets.append(ticket)
    return sum, new_tickets

def departure(tickets, dict, myticket):
    def isValid(value, values):
        if (value >= int(values[0]) and value <= int(values[1])) or (value >= int(values[2]) and value <= int(values[3])):
            return True
        return False

    dict_bools=defaultdict(list)
    for k,v in dict.items():
        for i in range(len(tickets[0])):
            nfc=True
            for j in range(len(tickets)):
                if not isValid(int(tickets[j][i]), v):
                    nfc=False
                    break
            dict_bools[k].append(nfc)

    rows = [None] * len(dict_bools.keys())
    while rows.count(None) != 0:
        for k,v in dict_bools.items():
            if v.count(True) == 1:
                index=v.index(True)
                rows[index] = k
                for v in dict_bools.values():
                    v[index] = 'done'
                break
        del dict_bools[k]

    multiply = 1
    for i,f in enumerate(rows):
        if 'departure' in f:
            multiply *= int(myticket[i])
    return(multiply)



fields=[]
tickets=[]
check = 0

for line in open(r'input.txt', 'r'):
    line = line[:-1]
    if line == "your ticket:":
        check = 1
        continue
    if line == "nearby tickets:":
        check = 2
        continue
    if line == "":
        continue
    if check == 0: fields.append(line.split(':'))
    elif check == 1: myticket = line.split(',')
    elif check == 2: tickets.append(line.split(','))

sum = 0

dict={field[0]: field[1].replace('or',' ').replace('-',' ').split() for field in fields}

part1, tickets = invalid(tickets,dict)

print(part1)

part2 = departure(tickets, dict, myticket)

print(part2)
