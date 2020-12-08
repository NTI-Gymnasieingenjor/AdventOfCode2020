import os

parentPath = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

desiredPath = "\\AdventOfCode2020\\solutions\\dag5\\dag5input.txt"

boardingPasses = open(parentPath + desiredPath).readlines()

# --------------------------------------------------------------- # 

count = 0
rowNumber = []
seatNumber = []
seatIDs = []

for i in boardingPasses:

    # Number of Rows is 128
    rowRange = list(range(0, 128))

    # Number of Seats per row is 8
    seatRange = list(range(0, 8))

    # Gets Rows
    Row = i.rpartition(i[6])
    Row = Row[0] + Row[1]

    for j in Row:
        if j == "F":
            rowLength = len(rowRange)
            rowRange = rowRange[:len(rowRange)//2]

        if j == "B":
            rowRange = rowRange[len(rowRange)//2:]

    # Gets Seats
    Seat = i.partition(i[7])
    Seat = Seat[1] + Seat[2]

    for k in Seat:
        if k == "R":
            seatRange = seatRange[len(seatRange)//2:]

        if k == "L":
            seatRange = seatRange[:len(seatRange)//2]

    seatNumber.append(seatRange[0])
    # print(count)
    # count += 1
    rowNumber.append(rowRange[0])

    seatID = rowRange[0] * 8 + seatRange[0]

    seatIDs.append(seatID)

print(seatIDs)
# sortedSeatIDs = sorted(seatIDs)
# print(sortedSeatIDs)

desiredNumber = sum(range(min(seatIDs), max(seatIDs) + 1))
missingNumber = sum(seatIDs)
actualNumber = desiredNumber - missingNumber
print(actualNumber)