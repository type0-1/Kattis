line = input()
line = line.split(" ") 
a = int(line[0])
b = int(line[1])

if a == b:
    print(a + 1)
else:
    if a > b:
        i = b
        while i <= a:
            print(i + 1)
            i += 1
    elif b > a:
        i = a
        while i <= b:
            print(i + 1)
            i += 1