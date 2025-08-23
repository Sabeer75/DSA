nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
n = len(nums)
K = k % n

l, r = 0, n - 1
while l < r:
    nums[l], nums[r] = nums[r], nums[l]
    l += 1
    r -= 1

l, r = 0, k - 1
while l < r:
    nums[l], nums[r] = nums[r], nums[l]
    l += 1
    r -= 1

l, r = k, n - 1
while l < r:
    nums[l], nums[r] = nums[r], nums[l]
    l += 1
    r -= 1
print(nums)


"""
nums = [-1, -100, 3, 99]
k = 2
res = []
l = 0
r = len(nums) - k
print(r)

while r <= len(nums) - 1:
    res.append(nums[r])
    r += 1
r = len(nums) - k
for i in range(l, r):
    res.append(nums[i])
print(res)
"""
