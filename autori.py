s = input()
i = 0
string = ""

while i < len(s):
    if ("A" <= s[i] and s[i] <= "Z"):
        string = string + s[i]
    i += 1
print(string)