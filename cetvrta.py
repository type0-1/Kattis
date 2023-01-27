i = 0
list = []
list2 = []
final = []
while i < 3:
    line = input()
    line = line.split(" ")
    list.append(line[0])
    list2.append(line[1])
    i += 1

if list[0] == list[1]:
    final.append(list[2])
elif list[1] == list[2]:
    final.append(list[0])
elif list[0] == list[2]:
    final.append(list[1])

if list2[0] == list2[1]:
    final.append(list2[2])
elif list2[1] == list2[2]:
    final.append(list2[0])
elif list2[0] == list2[2]:
    final.append(list2[1])

print(" ".join(final))