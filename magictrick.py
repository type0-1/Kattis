s = input()
i = 0
total = 1
while i < len(s):
    j = i + 1
    while j < len(s):
        if s[i] == s[j]:
            total = 0
        j += 1
    i += 1
print(total)