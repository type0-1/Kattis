n = int(input())
list = []
i = 0

while i < n:
    line = input()
    line = line.lower()
    j = 0
    while j < len(line):
        if line[j] == "p" or line[j] == "r":
            if line[j:j + 4] == "pink" or line[j: j + 4] == "rose":
                total = 1
                list.append(total)
                j = len(line)
        j += 1
    i += 1

if len(list) == 0:
    print("I must watch Star Wars with my daughter")
else:
    i = 0
    total = 0
    while i < len(list):
        total += list[i]
        i += 1
    print(total)
        