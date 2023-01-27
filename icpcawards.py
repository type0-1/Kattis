n = int(input())
list = []
i = 0
while i < n:
    line = input()
    name, team = line.split(" ")
    if name not in list:
        list.append(name)
        list.append(team)
    i += 1
i = 0
while i < 24:
    print(list[i], list[i + 1])
    i += 2