line = input()
x, y, n = line.split(" ")
x = int(x)
y = int(y) 
n= int(n)

i = 1
while i <= n:
    if i % x == 0 and i % y != 0:
        print("Fizz")
    elif i % y == 0 and i % x != 0:
        print("Buzz")
    elif i % x == 0 and i % y == 0:
        print("FizzBuzz")
    else:
        print(i)
    i += 1
    