passwordList = open("C:/Users/felix.larsson5\Documents/- Code Jam -/- Advent Of Code -/dag2/dag2input.txt").readlines()

trash = [i.split(' ')[1] for i in passwordList]

characterRange = [i.split(' ')[0] for i in passwordList]

maxRange = [i.split('-')[0] for i in characterRange]
minRange = [i.split('-')[1] for i in characterRange]

anotherCounter = 0

for i in maxRange:
    maxRange[anotherCounter] = int(maxRange[anotherCounter])
    minRange[anotherCounter] = int(minRange[anotherCounter])

    minRange[anotherCounter] -= 1
    maxRange[anotherCounter] -= 1

    anotherCounter += 1

typeOfCharacter = [i.split(':')[0] for i in trash]
actualPasswordList = [i.split(' ')[2] for i in passwordList]

print(len(passwordList))

counter = 0
validPasswords = 0

for i in passwordList:
    mini = minRange[counter]
    maxi = maxRange[counter] 
    actualPassword = actualPasswordList[counter]

    if actualPassword[mini] == typeOfCharacter[counter] and actualPassword[maxi] == typeOfCharacter[counter]:
        pass
    elif actualPassword[mini] == typeOfCharacter[counter] or actualPassword[maxi] == typeOfCharacter[counter]:
        validPasswords += 1

    

    counter += 1

print(validPasswords)