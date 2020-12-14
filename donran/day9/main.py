#!/usr/bin/env python3
import sys
data = list(map(lambda x: int(x), open("in").read().split("\n")[:-1]))
preamble = 25

def find(arr, ind, pre):
    found = False
    for i in range(ind-pre, ind):
        for j in range(ind-pre, ind):
            if i == j: continue
            if arr[i] + arr[j] == arr[ind]:
                found = True
                break
    return found

found = False
for i in range(preamble, len(data) - preamble):
    asd = find(data, i, preamble)
    if not asd:
        print("Star 1: {}".format(data[i]))
        found = data[i]
        break

if not found:
    print("could not find invalid number in set")
    sys.exit(1)

#Part two, bruteforce
for i in range(len(data)):
    for j in range(i, len(data)):
        s = [d for d in data[i:j]]
        if sum(s) > found:
            break
        if found == sum(s):
            print("Star 2: {}".format(min(s) + max(s)))
            sys.exit(1)
