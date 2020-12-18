#!/usr/bin/env python3

data = list(map(lambda x: int(x), open("10test.in", "r").read().split("\n")[:-1]))
data.sort()
data.append(max(data)+3)

def part1():
    one_jumps = 0
    two_jumps = 0
    three_jumps = 0

    current_num = 0
    i = 0
    while i <= len(data):
        if current_num+1 in data:
            current_num+=1
            one_jumps+=1
        elif current_num+2 in data:
            current_num+=2
            two_jumps+=1
        elif current_num+3 in data:
            current_num+=3
            three_jumps+=1
        i+=1

    return one_jumps * three_jumps

