usedMod = []
usedNums = []
for i in range(0, 10):
    n = int(input())
    check = n % 42
    if n not in usedNums:
        if check not in usedMod:
            usedMod.append(check)
print(len(usedMod))
