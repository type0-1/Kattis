n = int(input())
i = 0
while i < n:
    line = input()
    list = line.split(" ")
    j = 1
    total = 0
    while j < (int(list[0]) + 1):
        total += int(list[j])
        j += 1
    total = (total - (int(list[0])) + 1)
    print(total)
    i += 1