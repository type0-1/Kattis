import sys
lines = sys.stdin.readlines()

numbers = lines[0].strip().split()
letters = lines[1].strip()
nums = []
for n in numbers:
    nums.append(int(n))
nums.sort()
output = ""
for c in letters:
    if c == "A":
        output += str(nums[0]) + " "
    if c == "B":
        output += str(nums[1]) + " "
    elif c == "C":
        output += str(nums[2]) + " "
print(output.strip())