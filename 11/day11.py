# It's far from the prettiest or the fastest code
# I've ever written, but it is what it is.
# I might rewrite it sometime in the future.

def part1(seats):
    old_seats=[]

    def rules(seats):
        directions=[(-1,0), (1,0), (0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1)]
        new_seats = []
        for i_row, row in enumerate(seats):
            new_seats.append('')
            for i_seat, seat in enumerate(row):
                count=0
                for direction in directions:
                    new_row = i_row + direction[0]
                    new_seat = i_seat + direction[1]

                    if new_row >= 0 and new_seat >= 0 and new_row < len(seats) and new_seat < len(row):
                        if seats[new_row][new_seat] == '#': count += 1

                if seat == 'L' and count == 0: new_seats[i_row] += '#'
                elif seat == '#' and count >= 4: new_seats[i_row] += 'L'
                else: new_seats[i_row] += seat

        return new_seats

    while old_seats != seats:
        old_seats, seats = seats, rules(seats)

    return sum([line.count('#') for line in seats])


def part2(seats):
    old_seats=[]

    def rules(seats):
        directions=[(-1,0), (1,0), (0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1)]
        new_seats = []
        for i_row, row in enumerate(seats):
            new_seats.append('')
            for i_seat, seat in enumerate(row):
                count=0
                for direction in directions:
                    new_row = i_row + direction[0]
                    new_seat = i_seat + direction[1]

                    while new_row >= 0 and new_seat >= 0 and new_row < len(seats) and new_seat < len(row):
                        if seats[new_row][new_seat] == '#': count += 1
                        if seats[new_row][new_seat] != '.': break
                        new_row = new_row + direction[0]
                        new_seat = new_seat + direction[1]

                if seat == 'L' and count == 0: new_seats[i_row] += '#'
                elif seat == '#' and count >= 5: new_seats[i_row] += 'L'
                else: new_seats[i_row] += seat

        return new_seats

    while old_seats != seats:
        old_seats, seats = seats, rules(seats)

    return sum([line.count('#') for line in seats])

seats = [line[:-1] for line in open(r'input.txt', 'r')]

print(part1(seats))
print(part2(seats))
