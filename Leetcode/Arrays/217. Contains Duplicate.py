from collections import defaultdict

nums = [1, 2, 3, 1]
duplicate = defaultdict(int)

for num in nums:
    duplicate[num] += 1

if any(i >= 2 for i in duplicate.values()):
    print("True")
else:
    print("False")
