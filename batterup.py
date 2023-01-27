n = int(input())
line = input()
line = line.split(" ")
list = []
i = 0
while i < len(line):
    if int(line[i]) > -1:
        list.append(int(line[i]))
    i += 1
i = 0
total = 0
while i < len(list):
    total += list[i]
    i += 1
print(total / len(list))
