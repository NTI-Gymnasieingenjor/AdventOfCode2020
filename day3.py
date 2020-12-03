#!/usr/bin/env python3
def fly_like_an_eagle(down, right):
    x = 0
    trees = 0
    for idx,row in enumerate(world):
        if idx % down == 0:
            if row[x%len(row)] == "#":
                trees += 1
            x+=right

    return trees


def part_one():
    print(fly_like_an_eagle(1, 3))


def part_two():
    instructions = [(1,1),(1,3),(1,5),(1,7),(2,1)]
    res = []
    for inst in instructions:
        res.append(fly_like_an_eagle(inst[0], inst[1]))

    answer = 1
    for r in res:
        answer *= r

    print(answer)


world = list(map(lambda x: x.replace("\n", ""), open("3.in").readlines()))

part_one()
part_two()
