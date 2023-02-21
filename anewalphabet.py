sentence = input().strip()
oldAlpha = "abcdefghijklmnopqrstuvwxyz"
newAlpha = ["@", "8", "(", "|)", "3", "#", "6", "[-]", "|", "_|", "|<", "1", "[]\/[]",
            "[]\[]", "0", "|D", "(,)", "|Z", "$", "']['", "|_|", "\/", "\/\/", "}{", "`/", "2"]
alphaDic = {}
zipped = zip(oldAlpha, newAlpha)
for character in zipped:
    alphaDic[character[0]] = character[1]
s = ""
zipped = zip(oldAlpha, newAlpha)
for c in sentence:
    if c.lower() in alphaDic:
        s += alphaDic[c.lower()]
    else:
        s += c
print(s)
