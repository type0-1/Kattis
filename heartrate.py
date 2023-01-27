t = int(input())
i = 0
while i < t:
    line = input()
    a, b = line.split(" ")
    a = int(a)
    b = float(b)
    minimum = (((15 / b) * (a - 1)) * 4)
    actual = (((15 / b) * a) * 4)
    maximum = (((15 / b) * (a + 1) * 4))
    print(round(minimum, 4), round(actual, 4), round(maximum, 4))
    i += 1
