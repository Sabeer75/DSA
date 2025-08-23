from collections import defaultdict

nums = [3, 2, 3]
n = len(nums) / 2
count = defaultdict(int)

for i in range(len(nums)):
    count[nums[i]] += 1
print(count)
for k, v in count.items():
    if v > n:
        print(k)
