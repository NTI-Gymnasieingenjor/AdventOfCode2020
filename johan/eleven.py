import sys

def solve():

    def check(data, line, char):
        count = 0
        for y in range(line):
            
        if(data[line-1][char-1] == '#'):
            count += 1
        if(data[line-1][char] == '#'):
            count += 1
        if(data[line-1][char+1] == '#'):
            count += 1
        if(data[line][char-1] == '#'):
            count += 1

        if(data[line][char+1] == '#'):
            count += 1
        if(data[line+1][char-1] == '#'):
            count += 1
        if(data[line+1][char] == '#'):
            count += 1
        if(data[line+1][char+1] == '#'):
            count += 1
        return count

    line = sys.stdin.readline().rstrip()
    data =[]

    val = "."*(len(line)+2)
    data.append(val)
    data.append('.'+line+'.')
    for line in sys.stdin:
        data.append('.'+line.rstrip()+'.')
    data.append(val)

    temp = []

    flag = True
    count = 0
    while(flag):
        count += 1
        temp = data.copy()
        print(temp)
        for line in range(1, len(temp)-1):
            for char in range(1, len(temp[line])- 1):
                result = check(temp, line, char)
                if(result == 0 and temp[line][char] == 'L'):
                    data[line] = data[line][:char] + '#' + data[line][char+1:]
                elif(result >= 4 and temp[line][char] == '#'):
                    data[line] = data[line][:char] + 'L' + data[line][char+1:]
        for line in data:
            print(line)
        #check convergence
        for index in range(len(data)):
            if(temp[index] != data[index]):
                flag = True
                break       
            flag = False
        print(flag)
    print(count)

    seat_count = 0
    for line in data:
        for char in line:
            if(char == '#'):
                seat_count += 1
    print(seat_count)
            
                
solve()
