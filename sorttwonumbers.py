line = input()
a, b = line.split(" ")

if int(a) < int(b):
    print(a, b)
else:
    print(b, a)