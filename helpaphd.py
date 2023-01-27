n = int(input())
i = 0

while i < n:
    line = input()
    j = 0
    while j < len(line):
        if line[j] == "+":
            line = line.split("+")
            print(int(line[0]) + int(line[1]))
        elif line == "P=NP":
            print("skipped")
            j = len(line)
        j += 1
    i += 1