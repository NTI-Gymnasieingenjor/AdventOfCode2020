#!/usr/bin/env python3
d = set(map(lambda x: int(x), open("1.in").readlines()))
# Fake onelinerz but still onelinerz
print([j*i for j in d for i in d if j+i == 2020][0])
# Part two
print([j*i*k for j in d for i in d for k in d if j+i+k == 2020][0])


## Actual onelinerz xD
# Part one
print([j*i for d in [set(map(lambda x: int(x), open("1.in").readlines()))] for j in d for i in d if j + i == 2020][0])
# Part two
print([j*i*k for d in [set(map(lambda x: int(x), open("1.in").readlines()))] for j in d for i in d for k in d if j + i + k == 2020][0])
