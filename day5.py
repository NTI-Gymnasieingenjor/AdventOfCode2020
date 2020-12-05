#!/usr/bin/env python3

data = list(map(lambda x: x.replace("\n", ""), open("5.in").readlines()))

def generate_ids():
    boarding_pass_ids = []
    for bp in data:
        rr = list(range(128))
        cr = list(range(8))
        row = None
        col = None
        for idx, letter in enumerate(bp):
            rindex = round((len(rr) - 1) / 2)
            cindex = round((len(cr) - 1) / 2)
            if letter == "F":
                if(idx != 6):
                    rr = rr[:rindex]
                else:
                    row = rr[0]
            elif letter == "B":
                if(idx != 6):
                    rr = rr[rindex:]
                else:
                    row = rr[1]
            elif letter == "L":
                if(idx != 9):
                    cr = cr[:cindex]
                else:
                    col = cr[0]
            else:
                if(idx != 9):
                    cr = cr[cindex:]
                else:
                    col = cr[1]

        boarding_pass_ids.append(row * 8 + col)

    return boarding_pass_ids

def part1():
    print("Part 1: {}".format(max(generate_ids())))

def part2():
    board_pass_ids = generate_ids()
    unique_ids = []
    for ID in board_pass_ids:
        if((ID+1) not in board_pass_ids) or (ID-1 not in board_pass_ids):
            unique_ids.append(ID)

    for ID in unique_ids:
        for ID2 in unique_ids:
            if(ID-ID2 == 2):
                print("Part 2: {}".format((ID+ID2)/2))

part1()
part2()
