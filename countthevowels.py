s = input()
i = 0
total = 0
while i < len(s):
    if s[i] == "a" or s[i] == "A":
        total += 1
    elif s[i] == "e" or s[i] == "E":
        total += 1
    elif s[i] == "i" or s[i] == "I":
        total += 1
    elif s[i] == "o" or s[i] == "O":
        total += 1
    elif s[i] == "u" or s[i] == "U":
        total += 1
    i += 1
print(total)