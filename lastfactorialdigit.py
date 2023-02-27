n = int(input())

for i in range(n):
    num = int(input())
    i = num - 1
    while i > 0:
        num *= i
        i -= 1
    print(str(num)[-1])
