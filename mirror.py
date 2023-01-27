n = int(input())
i = 0
while i < n:
    j = 0
    line = input()
    a, b = line.split(" ")
    a = int(a)
    b = int(b)
    list = []
    while j < a:
        inputs = input()
        list.append(inputs)
        j += 1
    j = 0
    total = 0
    while j < len(list):
        string = ""
        pos = list[len(list) - j - 1]
        string = pos + string
        if j == 0:
            print("Test", (i + 1))
            print(string[::-1])
        else:
            print(string[::-1])
        j += 1
    i += 1