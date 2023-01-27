s = input()
i = 0
count = 0

while i < 1:
    j = 0
    while j < len(s):
        if s[j] == "e":
            count += 1
        j += 1
    i += 1
print(s[0] + ("e" * (count * 2)) + s[len(s) - 1])