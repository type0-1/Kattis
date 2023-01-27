s = input()
i = 0

while i < len(s) and s[i] != "a":
    i += 1
if i < len(s):
    print(s[i:])