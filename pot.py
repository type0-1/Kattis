n = int(input())
i = 1
nums = []
while i <= n:
    line = input()
    nums.append(int(line[0:len(line) - 1]) ** int(line[len(line) - 1]))
    i += 1
i = 0
total = 0
while i < len(nums):
    total += nums[i]
    i += 1
print(total)