#!/usr/bin/env python3

data = list(map(lambda x: int(x), open("in_test").read().split("\n")[:-1]))

diffs = [-1,0,0,0]
curr = 0
data.sort()
for d in data:
    diff = abs(curr - d)
    if diff > 3:
        break
    diffs[diff] += 1
    curr = d
diffs[3] += 1
print(data)
goal = diffs[1]*diffs[3]
print(goal)


ma = data[len(data)-1]
def rec(arr, ind):
    tot = 0
    for i, d in enumerate(data):
        if i <= ind: continue
        if arr[ind]+3 >= ma:
            return 1
        elif arr[ind]+3 >= d:
            tot += rec(arr, i)
        elif arr[ind]+3 < d:
            continue
    return tot

print(rec(data, 0))
