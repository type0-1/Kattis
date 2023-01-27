n = int(input())
i = 0
prev = 0
curr = 1
list = []
while i < n:
    if i == 0:
        curr = prev
        prev = int(input())
        list.append(prev)
    else:
        total = 0
        curr = prev
        prev = int(input())
        list.append(prev)
    i += 1

list2 = []
total = 0
i = 0

if n % 2 != 0:
    print("still running")
else:
    while i + 1 < len(list):
        result = list[i + 1] - list[i]
        list2.append(result)
        i += 2
    i = 0
    total = 0
    while i < len(list2):
        total += list2[i]
        i += 1
    print(total)
