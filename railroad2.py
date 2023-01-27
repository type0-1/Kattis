info = input().split()
possibleOne = int(info[1]) % 2 == 0

if possibleOne:
    print("possible")
else:
    print("impossible")