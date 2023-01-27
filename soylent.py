import math
tests = int(input())

for i in range(tests):
    eachBottle = 400
    calorieIntake = int(input())
    result = int(math.ceil(calorieIntake / eachBottle))
    print(result)