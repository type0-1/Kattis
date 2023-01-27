topScore = 0
topContestant = 0

for contestantNumber in range(1, 6):
    total = 0
    grade = input().split()
    for i in grade:
        total += int(i)
    if total > topScore:
        topScore = total
        topContestant = contestantNumber

print(topContestant, topScore)
    