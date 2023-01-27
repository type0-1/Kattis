n = int(input())
pointsperside = 2
i = 0
while i < n:
    pointsperside += pointsperside - 1
    i += 1
print(pointsperside * pointsperside)