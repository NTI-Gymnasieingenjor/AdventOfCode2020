#!/usr/bin/env python3

data = []
with open("2.in", "r") as fd:
    data = fd.readlines()
    data = list(map(lambda x: x.replace("\n", ""),data))

def part1():
    valid_passwords = 0
    for line in data:
        rangee, char, password = line.split(" ")
        min_count, max_count = rangee.split("-")
        char = char[0]
        char_count = password.count(char)
        if(char_count >= int(min_count) and char_count <= int(max_count)):
            valid_passwords+=1
    return valid_passwords

def part2():
    valid_passwords = 0
    for line in data:
        rangee, char, password = line.split(" ")
        first, second = rangee.split("-")
        if bool(password[int(first)-1] == char[0]) != bool(password[int(second)-1] == char[0]):
            valid_passwords+=1
    return valid_passwords

print(part1())
print(part2())
