line = input()
a_total = 0
b_total = 0
i = 1
while i < len(line):
    char = line[i - 1]
    num = int(line[i])
    if char == "A":
        a_total += num
    elif char == "B":
        b_total += num
    i += 2
if a_total >= (b_total + 2):
    print("A")
elif b_total >= (a_total + 2):
    print("B")
    