# Advent of Code Day 3.1
import os

parentPath = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

desiredPath = "\\AdventOfCode2020\\solutions\\dag3\\dag3input.txt"

road = open(parentPath + desiredPath).readlines()

incrementY = 1
incrementX = 3

posY = incrementY
posX = incrementX

treeCounter = 0

for i in road:
    if posY > len(road) - 1:
        break
    
    roadMax = len(i) - 1
    if posX >= roadMax:
        posX = posX - roadMax

    if road[posY][posX] == "#":
        print("posY", posY)
        print("posX", posX)
        print("---")
        treeCounter += 1

    # print(posX)
    # print("posY", posY)

    posY += incrementY
    posX += incrementX

print("Trees:", treeCounter)
print(len(road))