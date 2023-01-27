cost = float(input())
lawns = int(input())
list = []
i = 0
while i < lawns:
    amount = 0
    line = input()
    w, h = line.split(" ")
    amount = (float(w) * float(h)) * cost
    list.append(amount)
    i += 1
i = 0
total = 0
while i < len(list):
    total = total + list[i]
    i += 1
print(total)