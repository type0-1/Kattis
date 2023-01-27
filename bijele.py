line = input()
piece = line.split(" ")
sop = [1, 1, 2, 2, 2, 8]
pieces = []
i = 0
while i < len(piece):
    pieces.append(int(piece[i]))
    i += 1
i = 0
s = ""
while i < len(pieces):
    if pieces[i] > sop[i]:
        result = (pieces[i] - sop[i])
    else:
        result = (pieces[i] - sop[i])
    s += str(int(result) * -1) + " "
    i += 1
print(s)