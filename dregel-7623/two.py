import sys

valid_password = 0

for line in sys.stdin:
    (count, char, password) = line.rstrip().split(" ")
    (min, max) = count.split("-")
    min = int(min) -1
    max = int(max) -1
    char = char.replace(":", '')

    or_pass = (password[min] == char) or (password[max] == char)
    and_pass = (password[min] == char) and (password[max] == char)

    if (or_pass and not and_pass):
        valid_password += 1

    
    #print(count, char, password)
    #print(min, max)

print(valid_password)

def part_one():
    valid_password = 0

    for line in sys.stdin:
        (count, char, password) = line.rstrip().split(" ")
        (min, max) = count.split("-")
        char = char.replace(":", '')

        if(int(min) <= password.count(char) <= int(max)):
            valid_password += 1
        
        #print(count, char, password)
        #print(min, max)

    print(valid_password)