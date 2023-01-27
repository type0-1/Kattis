x = int(input())
n = int(input())
i = 0
total = 0
while i < n:
    bytes = int(input())
    if bytes == x:
        total += 0
    else:
        total += (x - bytes)
    i += 1
print(total + x)