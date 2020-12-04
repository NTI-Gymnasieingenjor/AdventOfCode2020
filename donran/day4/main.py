#!/usr/bin/env python3
import re
data = "".join(open("in").readlines()).split("\n\n")
reg = {
    "byr": "(19[2-8][0-9]|199[0-9]|200[0-2])",
    "iyr": "(201[0-9]|2020)",
    "eyr": "(202[0-9]|2030)",
    "hgt": "(59|6[0-9]|7[0-6])in|(1[5-8][0-9]|19[0-3])cm",
    "hcl": "\#[0-9a-f]{6}",
    "ecl": "amb|blu|brn|gry|grn|hzl|oth",
    "pid": "^\d{9}$"
}
valid = 0
for d in data:
    if all([False if d.count(a) == 0 else True for a in reg]):
        valid += 1

print("Star 1: {}".format(valid))
valid = 0
for i in range(len(data)):
    data[i] = data[i].replace("\n", " ").split(" ")
    v = 0
    for a in data[i]:
        if a == "": continue
        (key, value) = a.split(":")
        if key in reg and re.match(reg[key], value):
            v += 1
    if v == len(reg):
        valid += 1
print("Star 2: {}".format(valid))
