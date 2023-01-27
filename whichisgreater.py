line = input()
a, b = line.split(" ")

if int(a) > int(b):
    print("1")
elif int(a) <= int(b):
    print("0")