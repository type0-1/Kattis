data = input().split()
totalJudges = int(data[0])
alreadyRated = int(data[1])

missingRatings = totalJudges - alreadyRated
minimum = missingRatings * -3
maximum = missingRatings * 3
total = 0

for i in range(alreadyRated):
    ratings = int(input())
    total += ratings
print(((total + minimum) / totalJudges), ((total + maximum) / totalJudges))
    