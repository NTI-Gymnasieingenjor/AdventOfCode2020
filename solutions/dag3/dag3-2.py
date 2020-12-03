# Advent of Code Day 3.2

road = open("C:/Users/felix.larsson5/Documents/- Code Jam -/- Advent Of Code -/dag3/dag3input.txt").readlines()

incrementY = 2
incrementX = 1

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