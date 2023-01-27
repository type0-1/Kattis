line = input()
values = line.split(" ")
list = ["A 11 11", "K 4 4", "Q 3 3", "J 20 2", "T 10 10", "9 14 0", "8 0 0 ", "7 0 0"]
i = 0
total = 0 
while i < (int(values[0]) * 4):
    inputs = input()
    j = 0
    while j < len(list):
        split = list[j].split(" ")
        if inputs[0] == split[0] and inputs[1] == values[1]:
            total += int(split[1])
        elif inputs[0] == split[0] and inputs[1] != values[1]:
            total += int(split[2])
        j += 1
    i += 1
print(total)