line = input()
whsp = 0
lower = 0
upper = 0
symbols = 0
i = 0

while i < len(line):
    if ("A" <= line[i] and line[i] <= "Z"):
       upper += 1
    elif ("a" <= line[i] and line[i] <= "z"):
        lower += 1
    elif line[i] == "_":
        whsp += 1
    else:
        symbols += 1
    i += 1
print(round(whsp / len(line), 6))
print(round(lower / len(line), 6))
print(round(upper / len(line), 6))
print(round(symbols / len(line), 6))