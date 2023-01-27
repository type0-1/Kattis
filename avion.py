total = 0
i = 1
positions = []
while i < 6:
    line = input()
    j = 0
    while j < len(line):
        if line[j] == "F":
            if line[j:j + 3] == "FBI":
                positions.append(str(i))
        elif line[j] == "C":
            if line[j:j + 3] == "CIA":
                print("HE GOT AWAY!")
                i = 5
        j += 1
    i += 1

if len(positions) > 0:
    i = 0
    numbers = ""
    while i < len(positions):
        if i == 0:
            numbers = numbers + positions[i]
        else:
            numbers = numbers + " " + positions[i]
        i += 1
    print(numbers)
    