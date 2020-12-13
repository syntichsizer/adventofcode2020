from math import gcd

def wait(buses):
    min = float('inf')
    min_id = None

    for bus in buses[1]:
        count=0
        if bus != 'x':
            while count <= int(buses[0]):
                count += int(bus)
            if count < min:
                min = count
                min_id = int(bus)
    return (min - int(buses[0])) * min_id

# Part 2 using first bus. Works but it's too slow for puzzle input.

# def contest(buses):
#     minutes={}
#
#     for index, bus in enumerate(buses[1:], 1):
#         if bus != 'x':
#             minutes[index] = int(bus)
#
#     curr_min=int(buses[0])
#     while True:
#         count=0
#         for k,v in minutes.items():
#             if (curr_min + k) % v != 0:
#                 break
#             else:
#                 count += 1
#         if count == len(minutes):
#             break
#         curr_min += int(buses[0])
#
#     print(curr_min)

# Part 2 using bus with largest time. A bit faster but still too slow.

# def contest(buses):
#     minutes={}
#
#     for index, bus in enumerate(buses):
#         if bus != 'x':
#             minutes[index] = int(bus)
#
#     maxindex = max(minutes, key = minutes.get)
#     curr_min=int(minutes[maxindex])
#
#     while True:
#         count=0
#         for k,v in minutes.items():
#             if k != maxindex:
#                 min = curr_min + (k-maxindex) if k > maxindex else curr_min - (maxindex-k)
#                 #print(min)
#                 if (min) % v != 0:
#                     break
#                 else:
#                     count += 1
#         if count == len(minutes)-1:
#             break
#         curr_min += int(minutes[maxindex])
#         #print(curr_min)
#     return(curr_min-maxindex)


# After some time, I found out about "Chinese remainder theorem" on Reddit.

def contest(buses):

    def lcm(a, b):
        return abs(a*b) // gcd(a, b)

    minutes={}

    for index, bus in enumerate(buses[1:], 1):
        if bus != 'x':
            minutes[index] = int(bus)

    curr_min = int(buses[0])
    interval = int(buses[0])

    for k,v in minutes.items():
        while (curr_min + k) % v != 0:
            curr_min += interval
        interval = lcm(interval, v)
    return curr_min


buses = [line[:-1] for line in open(r'input.txt', 'r')]

buses[1] = buses[1].split(',')

print(wait(buses))

print(contest(buses[1]))
