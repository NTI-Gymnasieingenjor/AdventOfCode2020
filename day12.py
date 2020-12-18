#!/usr/bin/env python3


data = open("12test.in", "r").read().split("\n")[:-1]

y = 0
x = 0

directions = ["north", "west", "south", "east"]
forward_idx = 3

for row in data:
    action = row[0]
    value = row[1:]

    if(action == "F"):
        if(directions[forward_idx] == "north"):
            y += int(value)
        elif(directions[forward_idx] == "south"):
            y -= int(value)
        elif(directions[forward_idx] == "east"):
            x -= int(value)
        elif(directions[forward_idx] == "west"):
            x += int(value)
    elif(action == "L"):
        dr = int(value) / 90

        if(forward_idx == 0):
            forward_idx = len(directions) - 1
        else:
            forward_idx -= 1
    elif(action == "R"):
        if(forward_idx >= len(directions) - 1):
            forward_idx = 0
        else:
            forward_idx += 1
    else:
        if(action == "N"):
            y += int(value)
        elif(action == "S"):
            y -= int(value)
        elif(action == "W"):
            x += int(value)
        elif(action == "E"):
            x -= int(value)

print(y)
print(x)
print(y + x)
