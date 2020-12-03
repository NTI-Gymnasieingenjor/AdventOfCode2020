from inputs import nums

antal_first = 0
antal_second = 0
checker_first = 0
checker_second = 0

for num in nums:
    if (nums[checker_first][3]).count(nums[checker_first][2]) >= nums[checker_first][0]:
        if (nums[checker_first][3]).count(nums[checker_first][2]) <= nums[checker_first][1]:
            print(nums[checker_first])
            antal_first += 1
            checker_first = checker_first + 1
        else:
            print("nej")
            checker_first = checker_first + 1
    else:
        print("nej")
        checker_first = checker_first + 1



maximal = (nums[checker_second][1])
minimum = (nums[checker_second][0])
for num in nums:
    maximal = (nums[checker_second][1]) - 1
    minimum = (nums[checker_second][0]) - 1
    bokstav = (nums[checker_second][2])
    password = (nums[checker_second][3])
    max_position = (nums[checker_second][3][maximal])
    min_position = (nums[checker_second][3][minimum])

    
    if max_position == bokstav and min_position != bokstav:
        print(nums[checker_second])
        antal_second += 1

    elif min_position == bokstav and max_position != bokstav:
        print(nums[checker_second])
        antal_second += 1

    if checker_second >= 999:
        break

    checker_second = checker_second + 1
print ("Första är", antal_first)
print ("Andra är", antal_second)
