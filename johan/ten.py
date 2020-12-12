import sys

def solve_b2():
    data = [int(line.rstrip()) for line in sys.stdin]
    data.append(0)
    data.sort()
    data.reverse()

    lookup = dict()

    print(data)
    count = 1
    lookup[data[0]] = 1
    lookup[data[1]] = 1
    if(data[2] - data[0] > 3):
        lookup[data[2]] = 1
    else:
        lookup[data[2]] = lookup[data[0]] + lookup[data[1]]
        
    print(data[0])
    print(lookup[data[0]])
    print(data[1])
    print(lookup[data[1]])
    print(data[2])
    print(lookup[data[2]])
    
    index = 3
    while (index < len(data)):
        print(data[index])
        if data[index-1] - data[index] <= 3:
            lookup[data[index]] = lookup[data[index-1]]
            if data[index-2] - data[index] <= 3:
                lookup[data[index]] += lookup[data[index-2]]
                if data[index-3] - data[index] <= 3:
                    lookup[data[index]] += lookup[data[index-3]]
        print(lookup[data[index]])
        index += 1
    print("count", lookup[0])


def solve_b():
    def recurs(data, solutions):
        if(str(data) in solutions):
            return
        solutions.add(str(data))

        for index in range(len(data)-2):
            temp = data.copy()
            if(data[index+2] - data[index] == 3):
                temp.remove(data[index+1])
                recurs(temp, solutions)
            elif(data[index+2] - data[index] == 2):
                temp.remove(data[index+1])
                recurs(temp, solutions)
        print(len(solutions))

    data = [int(line.rstrip()) for line in sys.stdin]

    data.append(0)
    data.append(max(data)+3)
    data.sort()

    solutions = set()

    recurs(data, solutions)
    print("count", len(solutions))


def solve_a():
    data = [int(line.rstrip()) for line in sys.stdin]

    data.append(0)
    data.append(max(data)+3)

    data.sort()

    diff = []
    for index in range(len(data)-1):
        diff.append(data[index+1] - data[index])

    print(data)
    print(diff.count(1))
    print(diff.count(2))
    print(diff.count(3))

solve_b2()

