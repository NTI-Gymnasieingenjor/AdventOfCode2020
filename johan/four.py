import sys

pass_valid = set(['byr',
'iyr',
'eyr',
'hgt',
'hcl',
'ecl',
'pid',
'cid',])

pass_valid_hack = set(['byr',
'iyr',
'eyr',
'hgt',
'hcl',
'ecl',
'pid',])

def validate(key, value):
    if(key == 'byr' and 1920 <= int(value) <= 2002 ):
        return True
    elif(key == 'iyr' and 2010 <= int(value) <= 2020):
        return True
    elif(key == 'eyr' and 2020 <= int(value) <= 2030):
        return True
    elif(key == 'hgt'):
        if(value[-2:] == 'cm'):
            if(150 <= int(value[:-2]) <= 193):
                return True
        elif(value[-2:] == 'in'):
            if(59 <= int(value[:-2]) <= 76):
                return True
    elif(key == 'hcl'):
        if(value[0] == '#'):
            if(int(value[1:], 16) >= 0):
                return True
    elif(key == 'ecl'):
        if(value == 'amb' or 
           value == 'blu' or 
           value == 'brn' or 
           value == 'gry' or 
           value == 'grn' or 
           value == 'hzl' or 
           value == 'oth'):
            return True
    elif(key == 'pid'):
        if(len(value) == 9 and int(value) >= 0):
            return True
    return False

def solve():
    valid_passport = 0
    pass_data = set()

    for line in sys.stdin:
        line = line.rstrip()
        if(len(line) != 0):
            #read in data
            passport = line.rstrip().split(" ")
            for item in passport:
                key, value = item.split(":")
                if(validate(key, value)):
                    pass_data.add(key)
        else:
            #new line check set equality
            print(pass_data)
            print(pass_valid)
            if(pass_data == pass_valid or pass_data == pass_valid_hack):
                print("valid")
                valid_passport += 1
            else:
                print("not valid")
            pass_data.clear()
            
    print(valid_passport)


solve()
