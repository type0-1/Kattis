numbers = []
i = 0

n = int(input())
while i < n:
    line = input()
    numbers.append(int(line))
    i += 1
    
i = 1
results = []
while i <= numbers[len(numbers) - 1]:
    j = 0
    check = 0
    while j < len(numbers):
        if i != numbers[j]:
            check += 1
        else:
            pass
        j += 1
    if check == n:
        results.append(i)
    else:
        pass
    i += 1
if len(results) == 0:
    print("good job")
else:
    i = 0
    while i < len(results):
        print(results[i])
        i += 1
