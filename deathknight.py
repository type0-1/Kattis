n = int(input())
i = 0
check = 0
while i < n:
    line = input()
    j = 1
    while j < len(line):
        if line[j - 1] == "C" and line[j] == "D":
            check += 1
        else:
            pass
        j += 1
    i += 1
print(n - check)