line = input()
w_total = 0
b_total = 0

i = 0
while i < len(line):
    if line[i] == "W":
        w_total += 1
    elif line[i] == "B":
        b_total += 1
    i += 1

if w_total == b_total:
    print(1)
else:
    print(0)