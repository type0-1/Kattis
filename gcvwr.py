line = input()
g, t, c = line.split(" ")
weight = (int(g) - int(t)) * 0.90
line2 = input()
line2 = line2.split(" ")

total = 0
i = 0
while i < len(line2):
    total = total + int(line2[i])
    i += 1
print(int(weight - total))