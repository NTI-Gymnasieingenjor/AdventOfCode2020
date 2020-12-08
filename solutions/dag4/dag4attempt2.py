import os

parentPath = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

desiredPath = "\\AdventOfCode2020\\solutions\\dag4\\dag4input.txt"

passportFileList = open(parentPath + desiredPath).readlines()

lastWasEmpty = True
listCounter = 0
passports = []

for i in passportFileList:
    if len(i) != 1:
        if lastWasEmpty:
            passports.append(i)
            currentListItem = i
            lastWasEmpty = False

        if lastWasEmpty == False:
            passports[listCounter] = passports[listCounter] , i

    elif len(i) == 1:
        lastWasEmpty = True
        listCounter += 1

passportAmount = len(passports)