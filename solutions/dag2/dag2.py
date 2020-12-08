import os

parentPath = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

desiredPath = "\\AdventOfCode2020\\solutions\\dag2\\dag2input.txt"

passwordList = open(parentPath + desiredPath).readlines()

trash = [i.split(' ')[1] for i in passwordList]

characterRange = [i.split(' ')[0] for i in passwordList]

maxRange = [i.split('-')[0] for i in characterRange]
minRange = [i.split('-')[1] for i in characterRange]

typeOfCharacter = [i.split(':')[0] for i in trash]
actualPasswordList = [i.split(' ')[2] for i in passwordList]

# print(len(passwordList))

counter = 0
validPasswords = 0

for i in passwordList:
    occurrences = actualPasswordList[counter].count(typeOfCharacter[counter])

    if occurrences >= int(maxRange[counter]) and occurrences <= int(minRange[counter]):
        validPasswords += 1

    counter += 1

print(validPasswords)