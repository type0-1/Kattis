n = int(input())
nums = []
i = 0
while i < n:
    m = int(input())
    nums.append(m)
    i += 1

i = 0
while i < len(nums):
    print(nums[len(nums) - i - 1])
    i += 1