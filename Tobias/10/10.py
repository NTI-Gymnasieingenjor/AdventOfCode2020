#Laddar in 10_puzzle_input.txt filen
with open("Tobias/10/10_puzzle_input.txt") as file:
    lines = [line.strip() for line in file]

# 0 jolts
chargingOutlet = 0

copatebleTo0Jolts = [
    '1',
    '2',
    '3'
]

jolt = chargingOutlet

# Kollar igenom listan en gång
def lookThoghListOnce():
    for i in lines:
        if jolt == 0:
            for conbatebleJolt in copatebleTo0Jolts:
                # print(conbatebleJolt)
                # print(i)
                if conbatebleJolt == i:
                    print(i)
                else:
                    break
        else:
            print("Else")
        # print()

# Kollar igenom hela listan lika många gånger som saker i listan
# for puzzelInput in lines:
lookThoghListOnce()
