n = int(input())
i = 0
while i < n:
    line = input()
    check = 0
    f, s, r = line.split(" ")
    f = int(f)
    s = int(s)
    r = int(r)
    if f + s == r:
        check = 1
    elif (f - s) == r or (s - f) == r:
        check = 1
    elif (f * s) == r:
        check = 1
    elif (f / s) == r or (s / f) == r:
        check = 1
    else:
        check = 0
    if check == 1:
        print("Possible")
    else:
        print("Impossible")
    i += 1