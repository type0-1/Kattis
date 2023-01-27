line = input()
results = []
i = 0
while i < len(line):
    if line[i] == ":" or line[i] == ";":
        if line[i:i + 2] == ":)" or line[i:i + 3] == ":-)":
            print(i)
        elif line[i:i + 2] == ";)" or line[i: i + 3] == ";-)":
            print(i)
        else:
            pass
    i += 1