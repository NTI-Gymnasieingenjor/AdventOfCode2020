inputDoc = open("input.txt")
bagsList = {e[0].strip(): e[1].rstrip(".").split(", ")
            for e in [x.replace("bags", "bag").split("contain") for x in inputDoc.read().split("\n")]}
inputDoc.close()

# PART 1
print("\nPART 1")

goldBags = 0
for item in bagsList:
    values = bagsList[item]
    found = False
    if "shiny gold bag" == item:
        continue
    while found == False:
        foundValues = set()
        if len(values) == 0:
            break
        for bag in values:
            bag = "".join(x for x in bag if not x.isdigit()).strip()
            if "shiny gold bag" == bag:
                goldBags += 1
                found = True
                break
            [foundValues.add(b) for b in bagsList[bag]] if "no other bag" != bag else None
        values = foundValues

print(goldBags)  # 248


# PART 2
print("\nPART 2")

bags = 0
values = bagsList["shiny gold bag"]
while True:
    foundValues = []
    for bag in values:
        num = int("".join(x for x in bag if x.isdigit()).strip())
        bag = "".join(x for x in bag if not x.isdigit()).strip()
        for count in range(num):
            bags += 1
            [foundValues.append(b) for b in bagsList[bag] if "no other bag" not in b]
    if len(foundValues) == 0:
        break
    values = foundValues

print(bags)  # 57281
