#!/usr/bin/env python3
import re

def part1():
    bg = "shinygold"
    rules = None
    bags = {}
    with open("7.in", "r") as fd:
        rules = fd.read().split("\n")[:-1]
        for rule in rules:
            bag_name = rule[:rule.index("bags")].rstrip().replace(" ", "")
            contains = re.sub(r'[0-9]+', '', rule[rule.index("contain")+8:]).replace(" ", "").replace(".", "")
            bags[bag_name] = contains

    bags_containing = []
    for key in bags.keys():
        if bg in bags[key]:
            bags_containing.append(key)

    for bag in bags_containing:
        for key in bags.keys():
            if bag in bags[key]:
                bags_containing.append(key)

    print(len(list(set(bags_containing))))


def check_bag(bagname, bags):
    tot = 0
    for bag in bags:
        if bagname == bag["name"]:
            for bg in bag["contains"]:
                if(bg["amount"] == "no"):
                    continue
                tot += int(bg["amount"]) + int(bg["amount"]) * check_bag(bg["name"], bags)
    return tot

def part2():
    bags = []
    with open("7.in", "r") as fd:
        rules = fd.read().split("\n")[:-1]
        for rule in rules:
            bag_name = rule[:rule.index("bags")].rstrip()
            contains = rule[rule.index("contain")+8:].replace(".", "").replace(" bags", "").replace(" bag", "")
            bags.append({"name": bag_name, "contains": list(map(lambda x: {"name": x[2:], "amount": x.split(" ")[0]},contains.split(", ")))})

    print(check_bag("shiny gold", bags))

part1()
part2()
