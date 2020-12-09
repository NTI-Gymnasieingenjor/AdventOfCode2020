import sys
from functools import reduce

problem = []
for line in sys.stdin:
    problem.append(line.rstrip())

def solve(problem, x_slope, y_slope):
    length = len(problem[0])
    y = 0
    hit_trees = 0
    for line_num in range(0, len(problem), x_slope):
        if(problem[line_num][y] == '#'):
            hit_trees += 1
        y += y_slope
        if(y >= length):
            y = y % length    

    return(hit_trees)

tests = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

answers = []
for a, b in tests:
    print(a, b)
    answers.append(solve(problem, b, a))    

print(answers)

solution = reduce(lambda a, b: a*b, answers, 1)

print(solution)
