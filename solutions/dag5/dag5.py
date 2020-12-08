import os

parentPath = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

desiredPath = "\\AdventOfCode2020\\solutions\\dag5\\dag5input.txt"

listWithThings = open(parentPath + desiredPath).readlines()

for i in listWithThings:
    print(i)