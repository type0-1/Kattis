n = int(input())

for i in range(n):
    line = input().split()
    eWithout = int(line[0])
    eWith = int(line[1])
    cAdvertise = int(line[2])
    
    doesntMatter = eWith - cAdvertise == eWithout
    advertise = eWith - cAdvertise > eWithout

    if doesntMatter:
        print("does not matter")
    elif advertise:
        print("advertise")
    else:
        print("do not advertise")