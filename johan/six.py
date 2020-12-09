import sys

group = []
counter = 0
total = 0

for line in sys.stdin:
    line = line.rstrip()
    if(line):
        counter += 1
        group.extend(list(line))
    else:
        print(f"before filter:\t {group}")
        group = list(filter(lambda x: group.count(x) == counter, group))
        print(f"after filter:\t {group}")
        print()
        total += len(set(group))
        group.clear()
        counter = 0

print(total)
    