num = int(input())
num = bin(num)
result = str(num[2:])

i = len(result) - 1
string = ""
while i > -1:
    string = result[len(result) - i - 1] + string
    i -= 1
print(int(string, 2))