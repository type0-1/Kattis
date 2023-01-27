s = input()
i = 0
left = 0
right = -1

while i < len(s) and s[i] != "(":
    left += 1
    i += 1
if i < len(s):
    j = i
    while j < len(s) and s[j] != ")":
        j += 1
    if j < len(s):
        p = j
        while p < len(s):
            right += 1
            p += 1

if right == left:
    print("correct")
else:
    print("fix")