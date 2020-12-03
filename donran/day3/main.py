#!/usr/bin/env python3
data = list(map(lambda x: x.replace("\n",""), open("in.day3", "r").readlines()))
print(sum([1 if d[x][(x*3)%len(d[x])]=="#" else 0 for d in [data] for x in range(len(d))]))

c = 1
li = []
inst = [(1,1), (1,3), (1,5), (1,7), (2,1)]
for q in range(len(inst)):
    co = 0
    x = 0
    for y in range(0, len(data), inst[q][0]):
        if data[y][x%len(data[y])] == "#":
            co += 1
        x += inst[q][1]
    li.append(co)
for co in li:
    c*=co
print(c)
