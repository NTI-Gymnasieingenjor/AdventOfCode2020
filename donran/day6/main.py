#!/usr/bin/env python3

data = open("in").read().split("\n\n")
data = list(map(lambda x: x.split("\n"), data))
for i in range(len(data)): # todo this is stupid
    data[i] = list(filter(lambda x: x != '', data[i]))

tot = 0
tot2 = 0
for d in data:
    a = set("".join(d))
    tot += len(a)
    tota = 0
    for q in a:
        if len(d) == len(list(filter(lambda x: x.count(q) > 0, d))):
            tot2 += 1
print(tot)
print(tot2)
