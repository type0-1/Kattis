line = input()

n1 = input()
n1 = n1.split(" ")
n2 = input()
n2 = n2.split(" ")
i = 0

while i < len(n2):
    j = 0
    while j < len(n1):
        if n2[i] == n1[j]:
            n1.pop(j)
        else:
            pass
        j += 1
    i += 1
i = 0
while i < len(n1):
    print(n1[i])
    i += 1