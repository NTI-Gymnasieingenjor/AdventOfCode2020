import math

inputDoc = open("input.txt")
docLines = list(map(lambda x: x.rstrip("\n"), inputDoc.readlines()))
inputDoc.close()

# PART 1
print("\nPART 1")

"""
The first 7 characters will either be F or B; 
these specify exactly one of the 128 rows on the plane
    Start by considering the whole range, rows 0 through 127.
    F means to take the lower half, keeping rows 0 through 63.
    B means to take the upper half, keeping rows 32 through 63.
    F means to take the lower half, keeping rows 32 through 47.
    B means to take the upper half, keeping rows 40 through 47.
    B keeps rows 44 through 47.
    F keeps rows 44 through 45.
    The final F keeps the lower of the two, row 44.

The last three characters will be either L or R; 
these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7)

L means to keep the lower half, while R means to keep the upper half
    Start by considering the whole range, columns 0 through 7
    R means to take the upper half, keeping columns 4 through 7.
    L means to take the lower half, keeping columns 4 through 5.
    The final R keeps the upper of the two, column 5.

FBFBBFFRLR: row 44, column 5

Seat ID = row * 8 + col
    BFFFBBFRRR: row 70, column 7, seat ID 567.
    FFFBBBFRRR: row 14, column 7, seat ID 119.
    BBFFBBFRLL: row 102, column 4, seat ID 820.

What is the highest seat ID on a boarding pass?
"""


def run(bPass: str):
    rgeFB = [0, 127]
    rgeLR = [0, 7]
    for char in bPass:
        if char == "F":
            rgeFB = list(map(lambda x: math.ceil(x), [rgeFB[0], (rgeFB[0] + rgeFB[1]) / 2]))
        elif char == "B":
            rgeFB = list(map(lambda x: math.ceil(x), [(rgeFB[0] + rgeFB[1]) / 2, rgeFB[1]]))
        elif char == "L":
            rgeLR = list(map(lambda x: math.floor(x), [rgeLR[0], (rgeLR[0] + rgeLR[1]) / 2]))
        elif char == "R":
            rgeLR = list(map(lambda x: math.floor(x), [(rgeLR[0] + rgeLR[1]) / 2, rgeLR[1]]))
    return min(rgeFB) * 8 + max(rgeLR)


assert run("BFFFBBFRRR") == 567
assert run("FFFBBBFRRR") == 119
assert run("BBFFBBFRLL") == 820

ids = [run(bpass) for bpass in docLines]
maxId = max(ids)
print(maxId)  # 951

# PART 2
print("\nPART 2")
# Find the missing ids between 1 and 951

print(next(filter(lambda x : x not in ids and (x > min(ids) or x > max(ids)), list(range(1, maxId + 1))))) # 653