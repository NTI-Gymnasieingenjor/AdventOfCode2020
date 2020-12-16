#!/usr/bin/env python3
import re, sys

data = open("in").read().split("\n")[:-1]

r = re.compile("^(.*) bags contain (.*)$")
for i in range(len(data)):
    m = re.search("^(.*) bags contain (.*)$", data[i])
    data[i] = []
    data[i].append( m.group(1))
    data[i].append(m.group(2)[:-1].split(","))
    data[i][1] = list(map(lambda x: x[1:] if x[0] == ' ' else x, data[i][1]))

start = "shiny gold"
baggers = []
def find(arr, bag):
    tot = 0
    for el in arr:
        for b in el[1]:
            cb = " ".join(b.split(" ")[1:-1])
            if bag in cb:
                baggers.append(el[0])
                tot += 1
                tot += find(arr, el[0])
                break
    return tot
yeet = find(data, start)
print("star 1: {}".format(len(set(baggers))))

def find2(arr, bag):
    tot = 0

    for el in arr:
        if el[0] == bag:
            for b in el[1]:
                if b[:2] == "no": continue
                c = int(b.split(" ")[0])
                cb = " ".join(b.split(" ")[1:-1])
                tot += c + c*find2(arr, cb)
    return tot

print("star 2: {}".format(find2(data, start)))

