line = input()
decimal = 0
i = 0
while i < len(line):
    decimal = decimal*2 + int(line[i])
    i += 1
result = str(oct(decimal))
print(result[2:])