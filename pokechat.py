line = input()
list = [" "]
numbers = []
i = 0
while i < len(line):
    list.append(line[i])
    i += 1
code = input()
i = 0
while i < len(code):
    numbers.append(int(code[i: i + 3]))
    i += 3
i = 0
string = ""
while i < len(numbers):
    pos = numbers[i]
    j = 0
    while j < len(list):
        if pos == j:
            string = string + list[j]
            j = len(list)
        j += 1 
    i += 1
print(string)