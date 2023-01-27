import math
width = int(input())
shatteredPieces = int(input())
total = 0
for i in range(shatteredPieces):
    piece = input().split()
    w = int(piece[0])
    l = int(piece[1])
    total += (w * l)
print(int(math.ceil(total / width)))