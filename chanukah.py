n = int(input())
list = []
i = 1

while i <= n:
    line = input()
    a, b = line.split(" ")
    j = int(b)
    total = 0
    while j > 0:
        total = total + j
        j -= 1
    list.append((str(i) + " " + str(total + int(b))))
    i += 1

i = 0
while i < len(list):
    print(list[i])
    i += 1