#!/usr/bin/env python3

def part1():
    groups = list(map(lambda x: x.replace("\n", ""), open("6.in").read().split("\n\n")))

    counts = []
    for group in groups:
        count = len(list(set(list(group))))
        counts.append(count)

    print(sum(counts))

def part2():
    groups = list(map(lambda x: x.split("\n"), open("6.in").read().split("\n\n")))

    counts = []
    for group in groups:
        group = list(filter(lambda x: x != "", group))
        qa = list(set(list("".join(group))))
        checks = list(map(lambda q: all(q in person for person in group), qa))
        count = len(list(filter(lambda x: x, checks)))
        counts.append(count)

    print(sum(counts))

print("PART 1")
part1()
print("PART 2")
part2()
