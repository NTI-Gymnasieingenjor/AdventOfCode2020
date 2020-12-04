from typing import List
import regex


inputDoc = open("input.txt")
# docLines = list(map(lambda x: x.rstrip("\n"), inputDoc.readlines()))
docLines = inputDoc.readlines()
inputDoc.close()

# PART 1
print("\nPART 1")
"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)

Missing cid is fine, but missing any other field is not
How many passports are valid?
"""
needed = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", ]

passports = list(map(lambda x: "", docLines))
index = 0
for item in docLines:
    if item[0] != "\n":
        passports[index] += (" " if passports[index] != "" else "") + item.rstrip("\n")
    else:
        index += 1

passports = list(filter(lambda x: True if x != "" else False, passports))

valid = 0
for item in passports:
    invalid = False
    for need in needed:
        if need not in list(map(lambda x: x.split(":")[0], item.split(" "))):
            invalid = True
            break
    if not invalid:
        valid += 1


print(valid)  # 237


# PART 2
print("\nPART 2")
"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.

iyr (Issue Year) - four digits; at least 2010 and at most 2020.

eyr (Expiration Year) - four digits; at least 2020 and at most 2030.

hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.

hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.

ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.

pid (Passport ID) - a nine-digit number, including leading zeroes.

cid (Country ID) - ignored, missing or not.
"""

needed = {
    "byr": [1920, 2002],
    "iyr": [2010, 2020],
    "eyr": [2020, 2030],
    "hgt": {"cm": [150, 193], "in": [59, 76]},
    "hcl": [[0, 9], ["a", "f"]],
    "ecl": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid":  9,
}

passports = list(map(lambda x: "", docLines))
index = 0
for item in docLines:
    if item[0] != "\n":
        passports[index] += (" " if passports[index] != "" else "") + item.rstrip("\n")
    else:
        index += 1

passports = list(filter(lambda x: x != "", passports))


# Should use regex in future...
def checkValid(split: List[str], need):
    item: str = dict(split)[need]
    if need == "byr" or need == "iyr" or need == "eyr":
        return needed[need][0] <= int(item) <= needed[need][1]
    elif need == "hgt":
        return (needed["hgt"][item[-2:]][0] <= int(item.replace(item[-2:], "")) <= needed["hgt"][item[-2:]][1]) if "cm" in item or "in" in item else False
    elif need == "hcl":
        return regex.match("^#([a-f0-9]{6})$", item)
    elif need == "ecl":
        return item in needed[need]
    elif need == "pid":
        return item.isdigit() and len(item) == 9
    return False


valid = 0
for item in passports:
    invalid = False
    split = list(map(lambda x: x.split(":"), item.split(" ")))
    for need in needed:
        if need not in list(map(lambda x: x[0], split)) or not checkValid(split, need):
            invalid = True
            break
    if not invalid:
        valid += 1

print(valid)  # 172
