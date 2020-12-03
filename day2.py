#!/usr/bin/env python3
data = list(map(lambda x: x.replace("\n", ""), open("in.day2").readlines()))
print("Star 1: {}".format(sum([1 if d[2].count(d[1]) >= d[0][0] and d[2].count(d[1]) <= d[0][1] else 0 for d in [(list(map(lambda x: int(x), d[0].split("-"))), d[1][0], d[2]) for d in [d.split(" ") for d in list(map(lambda x: x.replace("\n", ""), open("in.day2").readlines()))]]])))
print("star 2: {}".format([True if bool(d[2][d[0][0]] == d[1]) ^ bool(d[2][d[0][1]] == d[1]) else False for d in [(list(map(lambda x: int(x) - 1, d[0].split("-"))), d[1][0], d[2]) for d in [d.split(" ") for d in list(map(lambda x: x.replace("\n", ""), open("in.day2").readlines()))]]].count(True)))
