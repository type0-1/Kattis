n = int(input())
list = []
i = 0

while i < n:
    string = input()
    list.append(string)
    i += 1

i = 0
while i < len(list):
    if i % 2 == 0:
        print(list[i])
    i += 1