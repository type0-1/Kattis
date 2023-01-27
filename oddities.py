n = int(input())
i = 0

while i < n:
    num = int(input())
    if num % 2 == 0:
        print(str(num) + " is even")
    else:
        print(str(num) + " is odd")
    i += 1