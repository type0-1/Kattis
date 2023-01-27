line = input().split()
m = line[0]
d = int(line[1])

halloween = (m == "OCT" and d == 31)
christmas = (m == "DEC" and d == 25)

if halloween or christmas:
    print("yup")
else:
    print("nope")