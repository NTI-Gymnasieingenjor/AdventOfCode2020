#!/usr/bin/env python3
import re, sys
data = list(map(lambda x: x.replace("\n", " ").split(" "), open("in").read().split("\n\n")))
reg = {
    "byr": "(19[2-8][0-9]|199[0-9]|200[0-2])",
    "iyr": "(201[0-9]|2020)",
    "eyr": "(202[0-9]|2030)",
    "hgt": "(59|6[0-9]|7[0-6])in|(1[5-8][0-9]|19[0-3])cm",
    "hcl": "\#[0-9a-f]{6}",
    "ecl": "amb|blu|brn|gry|grn|hzl|oth",
    "pid": "^\d{9}$"
}
valid1 = 0
valid2 = 0
for d in data:
    v1 = 0
    v2 = 0
    for field in d:
        if field == "": continue
        (key, value) = field.split(":")

        if key in reg:
            v1 += 1
        else: continue

        if re.match(reg[key], value):
            v2 += 1
    valid1 += 1 if v1 == len(reg) else 0
    valid2 += 1 if v2 == len(reg) else 0
print("Star 1: {}".format(valid1))
print("Star 2: {}".format(valid2))
