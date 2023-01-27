n = int(input())
total = 0
i = 0

while i < n:
    num = int(input())
    total += num
    i += 1
print(total - (n - 1))