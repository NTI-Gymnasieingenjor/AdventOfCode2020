from typing import List


inputDoc = open("input.txt")
docLines = list(map(lambda x: x.split("\n"), inputDoc.read().split("\n\n")))
inputDoc.close()

# PART 1
print("\nPART 1")


def run(group: List[List[str]], all: bool = False):
    # yes = set([ans for person in group for ans in person])
    answers = dict()
    for person in group:
        for ans in person:
            if ans in answers:
                answers[ans] += 1
            else:
                answers[ans] = 1
    if all:
        answers = list(filter(lambda x: answers[x] == len(group), answers))
    return len(answers)


print(sum([run(e) for e in docLines]))  # 6170


# PART 2
print("\nPART 2")

print(sum([run(e, True) for e in docLines]))  # 2947
