import sys

def solve():
    max_id = 0
    boarding = []

    for line in sys.stdin:
        line = line.rstrip()
        
        print(line)
        row = line[:7].replace('B', '1').replace('F', '0')
        column = line[-3:].replace('R', '1').replace('L', '0')
        
        id = int(row, 2)*8+ int(column, 2)
        boarding.append(id)
        if(id > max_id):
            max_id = id
    print(max_id)
    boarding.sort()
    print(boarding)
    print(len(boarding))

    count = boarding[0]

    for number in boarding:
        print(count, number)
        if(number != count):
            print(count)
            return
        count += 1

solve()

