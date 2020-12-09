import sys

def solve_b():

    def recurs(bag_data, key):
        print("enter")
        temp_key_temp = key.split(" ")
        trim_key = temp_key_temp[1] + " " +temp_key_temp[2]
        print(trim_key)
        print(bag_data[trim_key])
        if(bag_data[trim_key] == ['no other bags.']):
            print(bag_data[trim_key], "['no other bags.']")
            print(int(temp_key_temp[0]))
            return int(temp_key_temp[0])
        else:
            print(key, bag_data[trim_key])
            count = 1
            for value in bag_data[trim_key]:
                print('value', value)
                count += recurs(bag_data, value)
            print("count", count)
            return (int(temp_key_temp[0])*count)
            
    bag_data = dict()
    for line in sys.stdin:
        line = line.rstrip()
        key_raw, value_raw = line.split(" contain ")
        value_raw = value_raw.split(", ")
        key_raw = key_raw.split(" ")
        #print(key_raw, value_raw)
        key_bag = str(key_raw[0] + " " + key_raw[1])
        value_bag = [" ".join(value.split(" ")[0:3]) for value in value_raw]
        bag_data[key_bag] = value_bag
    print(bag_data)

    result = recurs(bag_data, '1 shiny gold')
    print(result -1)

def solve_a():
    bag_data = dict()
    for line in sys.stdin:
        line = line.rstrip()
        print("line:", line)
        key_raw, value_raw = line.split(" contain ")
        value_raw = value_raw.split(", ")
        key_raw = key_raw.split(" ")
        print(key_raw, value_raw)
        key_bag = str(key_raw[0] + " " + key_raw[1])
        value_bag = []
        for value in value_raw:
            value = value.split(" ")
            value = value[1] + " " + value[2]
            print("value: ", value)
            if(value in bag_data):
                print("exists")
                print(bag_data[value])
                bag_data[value].append(key_bag)
            else:
                print("doesn't exist")
                bag_data[value] = [key_bag]
        print("bag_data, ", bag_data)
        print()

    explore = set(['shiny gold'])
    finished = set()

    while(explore):
        print("explore 1", explore)
        bag = explore.pop()
        print("pop: ", bag)
        finished.add(bag)
        if(bag in bag_data):
            result = set(bag_data[bag])
            print("explore 2", explore)
            print("result ", result)
            explore = explore.union(result)
            print(explore)
        print(finished)
        print()

    finished.remove('shiny gold')
    print(len(finished))

solve_b()