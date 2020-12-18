inputDoc = open("input.txt")
docLines = inputDoc.read().split("\n")
inputDoc.close()

# PART 1
print("\nPART 1")


"""
    acc increases or decreases a single global value called the accumulator by the value given in the argument.
    
    jmp jumps to a new instruction relative to itself.
    
    nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.

"""


def part1():
    accumulator, index = 0, 0
    executed = []
    while True:
        if index >= len(docLines):
            break
        name, number = tuple(docLines[index].split())
        number = int(number)
        if index in executed:
            break
        executed.append(index)
        if name == "jmp":
            index += number
        else:
            if name == "acc":
                accumulator += number
            index += 1
    return accumulator


print(part1())  # 1548


# PART 2
print("\nPART 2")


"""
Either a jmp is supposed to be a nop, or a nop is supposed to be a jmp.

The program is supposed to terminate by attempting to execute an instruction
immediately after the last instruction in the file.
By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.

Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). 
What is the value of the accumulator after the program terminates?
"""


def convert(name, number):
    if name == "jmp":
        name = "nop"
    elif name == "nop" and int(number) > 0:
        name = "jmp"
    return name, int(number)


def loopThrough(counter: int):
    accumulator, index = 0, 0
    lineUsed = []
    success = False
    while True:
        if index >= len(docLines):
            if accumulator > 0:
                success = True
            break
        if index in lineUsed:
            break
        else:
            lineUsed.append(index)
        name, number = tuple(docLines[index].split())
        number = int(number)
        if index == counter:
            name, number = convert(name, number)
        if name == "jmp":
            index += number
        else:
            if name == "acc":
                accumulator += number
            index += 1
    return success, accumulator


def part2():
    found = False
    accumulator, counter = 0, 0
    while found == False:
        found, accumulator = loopThrough(counter)
        counter += 1
    return accumulator


print(part2())  # 1375
