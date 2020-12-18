# ex: 1-4 m: mrfmmbjxr, How many are valid?
inputDoc = open("input.txt")
docLines = inputDoc.readlines()
inputDoc.close()


# PART 1
print("Part 1:", len(list(filter(lambda pas: True if int(pas.rstrip().split(":")[0].split(" ")[0].split("-")[0]) <= pas.rstrip().split(":")[1].replace(" ", "").count(pas.rstrip().split(":")[0].split(" ")[1]) <= int(pas.rstrip().split(":")[0].split(" ")[0].split("-")[1]) else False, docLines)))) # 607

# PART 2
# ONLY ONE SHOULD BE THE POS!
# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

# pas.rstrip().split(":")

print("Part 2:", len(list(filter(lambda pas: True if sum(list(map(lambda a: 1 if pas.rstrip().split(":")[1].replace(" ", "")[int(a) - 1] == pas.rstrip().split(":")[0].split(" ")[1] else 0, pas.rstrip().split(":")[0].split(" ")[0].split("-")))) == 1 else False, docLines))))  # 321
