#!/usr/bin/env python3

def part1():
    acc = 0
    data = open("8.in", "r").read().split("\n")
    inp_run = []
    inp = 0

    while inp < len(data) - 1:

        # Checks if instruction has run before.
        if inp in inp_run:
            print(acc)
            break

        instruction = data[inp]
        operation, value = data[inp].split(" ")
        inp_run.append(inp)
        if operation == "acc":
            acc += int(value)
            inp += 1
        elif operation == "jmp":
            inp += int(value)
        else:
            inp += 1

def simulate_cases(data):
    indices = [i for i, x in enumerate(data) if "nop" in x or "jmp" in x]

    cases = []
    for indx in indices:
        data_cp = data.copy()
        operation, value = data_cp[indx].split(" ")
        if(operation == "nop"):
            data_cp[indx] = "jmp " + value
        else:
            data_cp[indx] = "nop " + value

        cases.append(data_cp)

    return cases


def part2():
    data = open("8.in", "r").read().split("\n")
    simulated_cases = simulate_cases(data)

    for case in simulated_cases:
        acc = 0
        inp_run = []
        inp = 0

        notTeminated = False
        while inp < len(case) - 1:

            # Checks if instruction has run before.
            if inp in inp_run:
                notTeminated = True
                break

            operation, value = case[inp].split(" ")
            inp_run.append(inp)
            if operation == "acc":
                acc += int(value)
                inp += 1
            elif operation == "jmp":
                if int(value) == 0:
                    notTeminated = True
                    break
                inp += int(value)
            else:
                inp += 1

        if not notTeminated:
            print(acc)


part1()
part2()
