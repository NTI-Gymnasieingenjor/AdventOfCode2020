#!/usr/bin/env python3
data = open("in").read().split("\n")[:-1]
ran_inst = []
acc = 0

i = 0
while i < len(data):
    (inst, val) = data[i].split(" ")
    val = int(val)
    if i in ran_inst:
        break
    ran_inst.append(i)

    if inst == "nop":
        pass
    elif inst == "acc":
        acc += val
    elif inst == "jmp":
        i += val
        continue
    i += 1
print("star 1: {}".format(acc))

data2 = open("in").read().split("\n")[:-1]
for j in range(len(data2)):
    data = data2.copy()
    (dinst, dval) = data[j].split(" ")
    if dinst == "nop":
        dinst = "jmp"
    elif dinst == "jmp":
        dinst = "nop"
    data[j] = "{} {}".format(dinst, dval)
    inf = False
    ran_inst = []
    acc = 0
    i = 0
    while i < len(data):
        (inst, val) = data[i].split(" ")
        val = int(val)
        if i in ran_inst:
            inf = True
            break
        ran_inst.append(i)

        if inst == "nop":
            pass
        elif inst == "acc":
            acc += val
        elif inst == "jmp":
            i += val
            continue
        i += 1
    if not inf:
        print("star 2: {}".format(acc))
        break
