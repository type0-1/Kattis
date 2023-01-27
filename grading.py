line = input()

a, b, c, d, e = line.split(" ")
n = int(input())
if int(a) <= n:
    print("A")
elif int(b) <= n and n < int(a):
    print("B")
elif int(c) <= n and n < int(b):
    print("C")
elif int(d) <= n and n < int(c):
    print("D")
elif int(e) <= n and n < int(d):
    print("E")
elif n < int(e):
    print("F")