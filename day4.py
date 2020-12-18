#!/usr/bin/env python3

req_fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

def checka(name, value):
    isValid = True
    if(name == "byr"):
        if(len(value) == 4):
            value=int(value)
            if(value < 1920 or value > 2002):
                isValid = False
        else:
            isValid = False
    elif(name == "iyr"):
        if(len(value) == 4):
            value=int(value)
            if(value < 2010 or value > 2020):
                isValid = False
        else:
            isValid = False
    elif(name == "eyr"):
        if(len(value) == 4):
            value=int(value)
            if(value < 2020 or value > 2030):
                isValid = False
        else:
            isValid = False
    elif(name == "hgt"):
        if("cm" == value[-2:]):
            value = int(str(value).replace("cm", ""))
            if(value < 150 or value > 193):
                isValid = False
        elif("in" == value[-2:]):
            value = int(str(value).replace("in", ""))
            if(value < 59 or value > 76):
                isValid = False
        else:
            isValid = False
    elif(name == "hcl"):
        if("#" == value[0]):
            value = value.replace("#", "")
            if(len(value) == 6):
                valid_chars = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
                res = list(filter(lambda x: x in valid_chars,value))
                if(len(res) != 6):
                    isValid = False
            else:
                isValid = False
        else:
            isValid = False
    elif(name == "ecl"):
        valid_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if(len(value) == 3):
            if(value not in valid_colours):
                isValid = False
        else:
            isValid = False
    elif(name == "pid"):
        if(len(value) != 9 or not value.isnumeric()):
            isValid = False
    elif(name == "cid"):
        isValid = False

    return isValid

def is_valid(reqs):
    valids = 0
    for req in reqs:
        if(req == ""):
            continue
        name, value = req.split(":")
        if checka(name, value):
            valids += 1

    if(valids == 7):
        return True
    else:
        return False

def part1():
    data = None
    with open("4.in", "r") as fd:
        data = fd.read().split("\n\n")


    valid_pass = 0
    for paz in data:
        if all(x in paz for x in req_fields):
            valid_pass += 1

    print(valid_pass)

def part2():
    data = None
    with open("4pon.in", "r") as fd:
        data = fd.read().split("\n\n")
        data = list(map(lambda x: x.replace("\n", " "), data))

    valid_pass = 0
    for paz in data:
        reqs = paz.split(" ")
        if(is_valid(reqs)):
            valid_pass += 1

    print(valid_pass)


part2()
