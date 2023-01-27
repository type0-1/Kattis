
line = input()
a, b, c = line.split(" ")

one = (int(b) - int(a) - 1)
two = (int(c) - int(b) - 1)

if one > two:
    print(one)
else:
    print(two)