inputDoc = open("input.txt")
docLines = inputDoc.readlines()
inputDoc.close()

# PART 1
# Find two numbers that add up to 2020 and multiply them
correct1 = []
for line in docLines:
    line = int(line.replace("\n", ""))
    for lineTwo in docLines:
        lineTwo = int(lineTwo.replace("\n", ""))
        if line + lineTwo == 2020:
            correct1 = [line, lineTwo]
            break
    if len(correct1) > 0:
        break
print(correct1[0] * correct1[1])  # 514579

# PART 2
# Find 3 numbers that add to 2020
correct2 = []
for line in docLines:
    line = int(line.replace("\n", ""))
    for lineTwo in docLines:
        lineTwo = int(lineTwo.replace("\n", ""))
        for lineThree in docLines:
            lineThree = int(lineThree.replace("\n", ""))
            if line + lineTwo + lineThree == 2020:
                correct2 = [line, lineTwo, lineThree]
                break
        if len(correct2) > 0:
            break
    if len(correct2) > 0:
        break
print(correct2[0] * correct2[1] * correct2[2])  # 42275090
# print(next(map(lambda a: a[0] * a[1], [list(map(lambda a: int(a), filter(lambda a: [int(b) for b in docLines if int(a) + int(b) == 2020], docLines)))])))
