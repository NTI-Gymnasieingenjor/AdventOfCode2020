with open('inputs3.txt') as f:
    lines = f.readlines()

antal = 0
current_position = 0
current_line = 0
tred = 0
down = 2
right = 1

for f in range(323):

    if lines[current_line][current_position] == ".":
        antal = antal + 1
        current_line = current_line + down
        current_position = current_position + right     
    else:
        tred = tred + 1
        current_line = current_line + down
        current_position = current_position + right

    if current_line >= 323:
        print(tred)
        break
    else:
        pass

    if current_position >= 31:
        over_step = current_position - 31
        current_position = over_step
    else:
        pass

