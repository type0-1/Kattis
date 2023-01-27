t = input()
i = 0
check = 0
while i + 1 < len(t):
    if t[i] == "s":
        if t[i + 1] == "s":
            check = 1
            i = len(t)
    i += 1

if check == 0:
    print("no hiss")
else:
    print("hiss")