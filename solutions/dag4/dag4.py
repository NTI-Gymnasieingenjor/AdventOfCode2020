import re
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

        elif lastWasEmpty == False:
            passports[listCounter] = passports[listCounter] + i

    elif len(i) == 1:
        lastWasEmpty = True
        listCounter += 1

listCounter = 0
for i in passports:
#     passports[listCounter] = str(i).strip("()")
#     passports[listCounter] = str(passports[listCounter]).strip("'")
#     passports[listCounter] = str(passports[listCounter]).strip('\n','')
    passports[listCounter] = i.strip()
    listCounter += 1

# listCounter = 0
# for i in passports:
#     passports[listCounter] = str(passports[listCounter])
#     listCounter += 1
    
# passportsNew = []

# for element in passports:
#     passportsNew.append(element.strip("\n"))

for i in passports:
    print(str(i))

# validPassports = 0

# for i in passports:
#     # print("här är i --------", i)
#     if "byr" in i:
#         pass
#     elif "hcl" in i:
#         pass
#     elif "ecl" in i:
#         pass
#     elif "eyr" in i:
#         pass
#     elif "pid" in i:
#         pass
#     elif "hgt" in i:
#         pass
#     elif "iyr" in i:
#         validPassports += 1

print("\n hej: -- \n" + passports[253])

# print(validPassports)

print(len(passportFileList))
print(len(passports))
# print("lol:", passports[253])