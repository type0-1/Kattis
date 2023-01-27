n = int(input())
i = 0
while i < n:
    line = input()
    if line[0:10] == "simon says":
        print(line[11:])
    else:
        print("")
    i += 1