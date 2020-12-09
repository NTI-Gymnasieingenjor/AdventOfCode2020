import sys

def solve_b():
    key = 1398413738
    data = []

    for line in sys.stdin:
        data.append(int(line.rstrip()))

    for a in range(0, len(data)):
        candidate = []
        for b in range(a+1, len(data)):
            candidate.append(data[b])
            if(sum(candidate) < key):
                pass
            elif(sum(candidate) == key):
                print("finish")
                print(min(candidate) + max(candidate))
                return
            else:
                break    
            

def solve_a():

    data = []
    preamable = 25

    for line in sys.stdin:
        data.append(int(line.rstrip()))

    for index in range (preamable, len(data)):
        #print(data[index])
        hash_list = []
        for check in range(index-preamable, index):
            #print("     ", data[check])
            hash_list.append(data[check])

        flag = False
        for a in range(0, len(hash_list)):
            for b in range(0, len(hash_list)):
                #print(a, b, a+b)
                if(hash_list[a]+hash_list[b] == data[index] and
                    a != b):
                    print(hash_list[a], hash_list[b], '=', data[index])
                    flag = True
        if(flag == False):
            print("end", data[index])
            return

solve_b()
