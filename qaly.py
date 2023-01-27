n = int(input())

i = 0
total = 0

while i < n:
    line = input()
    a, b = line.split(" ")
    a = float(a)
    b = float(b)
    total = total + (a * b)
    i += 1
    
print(total)