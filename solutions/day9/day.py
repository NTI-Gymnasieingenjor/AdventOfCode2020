inputDoc = open("input.txt")
docLines = [int(i) for i in inputDoc.read().split("\n")]
inputDoc.close()

# PART 1
print("\nPART 1")


def findXMAS(preamble: int):
    for index, item in enumerate(docLines):
        if index < preamble:
            continue
        numbersBack = [i for i in docLines[index - preamble:index]]
        found = False
        for x in numbersBack:
            for y in numbersBack:
                if x == y:
                    continue
                if x+y == item:
                    found = True
                    break
            if found:
                break
        if not found:
            return item
    return 0


invalidNumber = findXMAS(preamble=25)
print(invalidNumber)  # 2089807806


# PART 2
print("\nPART 2")


def findXMASsum(invalid: int):
    found = False
    for index, startItem in enumerate(docLines):
        addition = startItem
        numbers = [startItem]
        for i, item in enumerate(docLines[index + 1:]):
            if item == invalid or addition + item > invalid:
                break
            if addition < invalid:
                addition += item
                numbers.append(item)
            if addition == invalid:
                found = True
                break
        if found:
            return numbers
    return []


part2 = findXMASsum(invalidNumber)

print(min(part2) + max(part2))  # 245848639
