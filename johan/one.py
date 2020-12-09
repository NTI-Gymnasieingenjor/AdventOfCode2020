import sys 

from functools import reduce
values = []

for line in sys.stdin:     
    values.append(int(line.rstrip()))

def solve(values):
    for number_one in values:
        for number_two in values:
            for number_three in values:
                if (number_one + number_two + number_three) == 2020:
                    print(number_one, number_two, number_three)
                    print(number_one + number_two + number_three)
                    print(number_one*number_two*number_three)
                    return


def solve_comp(v):
    result = set([a*b*c for a in v for b in v for c in v if a+b+c==2020])
    [a for a in v if [b for b in v if [c for c in v if a+b+c==2020]]]
    set([a*b*c for a in v for b in v for c in v if a+b+c==2020 ])
    print(result)
    print(reduce(lambda a, b: a*b, [a for a in v if [b for b in v if [c for c in v if a+b+c==2020]]], 1))

solve_comp(values)