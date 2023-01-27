n = int(input())
i = 0
results = []
while i < n:
    line = input()
    st, end = line.split(" ")
    j = int(st)
    while j <= int(end):
        if j not in results:
            results.append(j)
        else:
            pass
        j += 1
    i += 1
print(len(results))
