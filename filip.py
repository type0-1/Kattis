line = input()
a, b = line.split(" ")

new_a = a[len(a) - 1] + a[1:len(a) - 1] + a[0]
new_b = b[len(a) - 1] + b[1:len(b) - 1] + b[0]

if int(new_a) > int(new_b):
    print(new_a)
else:
    print(new_b)