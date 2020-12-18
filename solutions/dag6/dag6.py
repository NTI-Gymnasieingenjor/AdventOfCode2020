import os

parentPath = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

desiredPath = "\\AdventOfCode2020\\solutions\\dag6\\dag6input.txt"

input = open(parentPath + desiredPath).readlines()

# --------------------------------------------------------------- # 

counter = -1
lastWasEmpty = True
groupList = []

for i in input:

    if len(i) == 1:
        lastWasEmpty = True

    elif lastWasEmpty == True:
        counter += 1
        groupList.append(i.strip("\n"))
        lastWasEmpty = False

    else:
        groupList[counter] += " " + i.strip("\n")

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

occurrenceList = []

for i in groupList:
    occurrenceCounter = 0
    for letter in alphabet:
        if i.count(letter) > 0:
            occurrenceCounter += 1
    
    occurrenceList.append(occurrenceCounter)

print(sum(occurrenceList))