#!/usr/bin/env python3

t = int(input())
i = 0

while i < t:
    n = int(input())
    list = []
    j = 0
    while j < n:
        line = input()
        if line not in list:
            list.append(line)
        else:
            pass
        j += 1
    print(len(list))
    i += 1