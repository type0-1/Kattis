n = int(input())
line = input().split()
total = 0
for x in line:
    expense = int(x)
    if expense < 0:
        total += -expense
print(total)