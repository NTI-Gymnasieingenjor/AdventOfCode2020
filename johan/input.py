import sys
valid_password = 0

for line in sys.stdin:
    (count, char, password) = line.split(" ")
    (min, max) = count.split("-")
    char = char.replace(":", '')
    print(min, max, char, password)