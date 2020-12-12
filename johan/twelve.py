import sys

x = 0
y = 0
direction = 90

for line in sys.stdin:
    print(x, y, direction)
    command, value = line[0], int(line[1:])
    print(command, value)
    if(command == 'N'):
        y = y + value 
        pass
    elif(command == 'S'):
        y = y - value
        pass
    elif(command == 'E'):
        x = x + value
        pass
    elif(command == 'W'):
        x = x - value
        pass
    elif(command == 'L'):
        direction = (direction - value) % 360
        pass
    elif(command == 'R'):
        direction = (direction + value) % 360
        pass
    elif(command == 'F'):
        if(direction == 90):
            x = x + value
            pass
        elif(direction == 180):
            y = y - value
            pass
        elif(direction == 270):
            x = x - value
            pass
        elif(direction == 0):
            y = y + value
            pass
print(x, y)
print(abs(x)+abs(y))