#!/usr/bin/env python3
data = list(map(lambda x: int(x), open("9.in", "r").read().split("\n")[:-1]))


def get_premble(premble_nums):
    all_sums = []
    for num1 in premble_nums:
        for num2 in premble_nums:
            if(num1 != num2):
                all_sums.append(num1+num2)
    return all_sums

def find_invalid_num():
    premble_len = 25
    other_nums = data[premble_len:]

    for idx, num in enumerate(other_nums):
        premble = get_premble(data[(idx+premble_len)-premble_len:(idx+premble_len)])
        if(num not in premble):
            return num

def find_ecryption_weakness():
    invalid_num = find_invalid_num()
    sum_nums = []
    start = 0
    while start != len(data):
        count = 2
        while count != data.index(invalid_num):
            temp_arr = []
            for i in range(start, count):
                temp_arr.append(data[i])

            count += 1
            if sum(temp_arr) == invalid_num:
                sum_nums = temp_arr
                break
        start+=1
    return sum_nums

def part2():
    enc_weak = find_ecryption_weakness()
    min_val = min(enc_weak)
    max_val = max(enc_weak)
    print(max_val+min_val)

print(find_invalid_num())
part2()
