line = input()
words = line.split(" ")
check = 0
i = 0

while i + 1< len(words):
    pos = words[i]
    j = i + 1
    while j < len(words):
        if pos == words[j]:
            check = 1
        j += 1
    i += 1

if check == 1:
    print("no")
else:
    print("yes")