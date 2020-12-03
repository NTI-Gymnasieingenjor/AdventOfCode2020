#!/usr/bin/env python3
# Cheaters one-liner
da = set(map(lambda x: int(x), open("day1.in").readlines()))
print([i*j*k for i in da for j in da for k in da if i+j+k==2020][0])

#actual one-liner
print([i*j*k for d in [set(map(lambda x: int(x), open("day1.in").readlines()))] for i in d for j in d for k in d if i+j+k==2020][0])

#jöhån
print(reduce(lambda a, b: a*b, [a for a in v if [b for b in v if [c for c in v if a+b+c==2020]]], 1))
