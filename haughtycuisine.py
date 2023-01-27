n = int(input())
list = []
i = 0
while i < n:
    line = input()
    list.append(line)
    i += 1
i = 0
while i < len(list):
    j = 0
    while j < len(list):
        if int(list[i][0]) > int(list[j][0]):
            tmp = list[i]
            list[i] = list[j]
            list[j] = tmp
        j += 1
    i += 1
results = list[0]
results = results.split(" ")
i = 0
string = ""
while i < len(results):
    print(results[i])
    i += 1
