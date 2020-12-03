inputDoc = open("input.txt")
docLines = list(map(lambda x: x.rstrip("\n"), inputDoc.readlines()))
inputDoc.close()

# PART 1
trees = 0
xIndex = 0
yIndex = 0
toBreak = False
while toBreak == False:
    for i in range(4):
        if i >= 3:
            # Down
            yIndex += 1
        else:
            # Right
            xIndex += 1
            if len(docLines[yIndex]) <= xIndex:
                xIndex = 0

        if len(docLines) <= yIndex:
            toBreak = True
            break

        if docLines[yIndex][xIndex] == "#" and i >= 3:
            trees += 1

print(trees) # 156

# PART 2
trees = [0, 0, 0, 0, 0]
toCheck = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
index = 0
for cords in toCheck:
    xIndex = 0
    yIndex = 0
    toBreak = False
    while toBreak == False:
        for i in range(sum(cords)):
            if i >= cords[0]:
                # Down
                yIndex += 1
            else:
                # Right
                xIndex += 1
                if len(docLines[yIndex]) <= xIndex:
                    xIndex = 0

            if len(docLines) <= yIndex:
                toBreak = True
                break

            if docLines[yIndex][xIndex] == "#" and i >= sum(cords) - 1:
                trees[index] += 1
    index += 1

print(trees)

muli = 1
for mu in trees:
    muli *= mu if mu > 0 else 1

print("product:", muli) # 3521829480
