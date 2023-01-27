n = int(input())
i = 0

while i < n:
    line1 = input()
    line2 = input()
    string = ""
    j = 0
    while j < len(line1) and j < len(line2):
        if line1[j] == line2[j]:
            string = string + "."
        else:
            string = string + "*"
        j += 1
    print(line1)
    print(line2)
    print(string)
    i += 1