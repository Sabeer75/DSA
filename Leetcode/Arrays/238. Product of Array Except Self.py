nums = [1, 2, 3, 4]
n = len(nums)
res = [1] * n
# find mul of prefix for particular index
prefix = 1
for i in range(n):
    res[i] = prefix
    prefix *= nums[i]
# suffix of the current index in res
suffix = 1
for i in range(n - 1, -1, -1):
    res[i] *= suffix
    suffix *= nums[i]
print(res)
