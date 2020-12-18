import numpy
import math

inputDoc = open("input.txt")
docLines = sorted([int(i) for i in inputDoc.read().split("\n")])
inputDoc.close()

# PART 1
print("\nPART 1")


myJoltage = 0
adapterDiff = 3
myAdapter = max(docLines) + adapterDiff

listOfJolts = {1: [], 3: []}

for index, joltA in enumerate(docLines):
    if index + 1 < len(docLines):
        listOfJolts[docLines[index + 1] - joltA].append(index)

print(numpy.prod([len(listOfJolts[i]) + 1 for i in listOfJolts]))  # 1890


# PART 2
print("\nPART 2")

arrangements = set({})
# while count <= math.pow(len(docLines), 2):
# order = tuple()
count = 0
while count <= math.pow(len(docLines), 2):
    order = []
    for index, item in enumerate(docLines):
        if index + 1 >= len(docLines):
            if item + 3 == myAdapter:
                arrangements.add(tuple(order))
            break
        if 0 < docLines[index + 1] - item < adapterDiff + 1:
            order.append(item)
    count += 1
itertools.combinations()
print(arrangements)
