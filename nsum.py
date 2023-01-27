n = input()
line = input()
line = line.split(" ")
i = 0
total = 0
while i < len(line):
    total = total + int(line[i])
    i += 1
print(total)