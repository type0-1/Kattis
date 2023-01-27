line = input()
nums = []
i = 0
while i < len(line):
    if ("0" <= line[i] and line[i] <= "9"):
        nums.append(line[i])
    i += 1
i = 0
total = 0
while i < len(nums):
    if i == 0:
        total += (int(nums[i]) * 4)
    elif i == 1:
        total += (int(nums[i]) * 3)
    elif i == 2:
        total += (int(nums[i]) * 2)
    elif i == 3:
        total += (int(nums[i]) * 7)
    elif i == 4:
        total += (int(nums[i]) * 6)
    elif i == 5:
        total += (int(nums[i]) * 5)
    elif i == 6:
        total += (int(nums[i]) * 4)
    elif i == 7:
        total += (int(nums[i]) * 3)
    elif i == 8:
        total += (int(nums[i]) * 2)
    elif i == 9:
        total += (int(nums[i]) * 1)
    i += 1

if total % 11 == 0:
    print("1")
else:
    print("0")