line = input()
words = line.split(" ")
total = 0
i = 0
while i < len(words):
    pos = words[i]
    j = 0
    while j < len(pos):
        if pos[j:j + 2] == "ae":
            total += 1
            j = len(pos)
        j += 1
    i += 1
result = ((total / len(words)) * 100)
if result >= 40:
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")