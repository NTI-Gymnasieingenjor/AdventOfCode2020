import sys

def solve():
    program_src = []

    for line in sys.stdin:
        program_src.append(line.rstrip())

    finished = False

    change_index = 0
    count = 0
    while(not finished): 
        acc = 0
        flag = True
        position = 0
        order = []
        program = []
        program = program_src.copy()
        #print("change index", change_index)

        #for line in program:
        #    print(line)

        # change one jmp or nop
        for index in range(len(program)):
            op = program[index][0:3]
            if(op == 'nop' and index >= change_index):
                change_index = index
                #print("before",program[change_index] )
                program[change_index] = program[change_index].replace('nop', 'jmp')
                #print("after",program[change_index] )
                change_index += 1
                break
            elif(op == 'jmp' and index >= change_index):
                change_index = index
                #print("before",program[change_index] )
                program[change_index] = program[change_index].replace('jmp', 'nop')
                #print("after",program[change_index] )
                change_index += 1
                break
        #print("change", change_index)

        #for line in program:
        #    print(line)

        #run with the change

        while(flag):
            #print(position)
            #print(program[position])
            if(position >= len(program)):
                print("finish", position, order)
                flag = False
                finished = True
                break
            op = program[position][0:3]
            value = int(program[position][4:])
            if(position in order):
                print("loop", position, order)
                flag = False
                break
            order.append(position)
            if(op == 'nop'):
                pass
            elif(op == 'acc'):
                acc += value
                #print('acc', acc)
            elif(op == 'jmp'):
                position += value - 1
            else:
                print("error op code: ", op)
                return
            position += 1
        print("acc", acc)
        print("max: ", max(order))
        print()
        count += 1

solve()