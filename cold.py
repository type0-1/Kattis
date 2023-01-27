n = int(input())
nums = input()
nums = nums.split(" ")
total = 0

for num in nums:
    if int(num) < 0:
        total += 1
print(total)