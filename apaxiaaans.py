word = " " + input()
string = " "
i = 1

while i < len(word):
    if word[i] != word[i - 1]:
        string = string + word[i]
    i += 1
print(string)