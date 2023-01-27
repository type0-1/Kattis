line = input()
total1 = 0
i = 0
while i < len(line):
    if line[i] == "a":
        total1+= 1
    i += 1
total2 = 0
line = input()
i = 0
while i < len(line):
    if line[i] == "a":
        total2 += 1
    i += 1

if total1 < total2:
    print("no")
elif total2 <= total1:
    print("go")
    