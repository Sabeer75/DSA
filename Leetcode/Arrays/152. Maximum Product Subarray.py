# optiml using prefix suffix
nums = [1, 0, -1, 2, 3, -5, -2]
maxi = float("-inf")
prefix, suffix = 1, 1
for i in range(len(nums)):
    # if 0 comes reassign
    if prefix == 0:
        prefix = 1
    elif suffix == 0:
        suffix = 1
    # otherwise add all
    prefix *= nums[i]
    suffix *= nums[len(nums) - i - 1]
    # check max
    maxi = max(maxi, max(prefix, suffix))
print(maxi)


"""
# O(n) but 156/ 190 test case 
res = float("-inf")
mul = 1
for i in range(len(nums)):
    if nums[i] >= 1:
        mul *= nums[i]
        res = max(res, mul)

    elif nums[i] < 0:
        mul *= nums[i]
        res = max(mul, res)

    elif nums[i] == 0:
        mul = 1
        res = max(res, nums[i])
print(res)
"""


"""
#brute force 
nums = [3,-1,4]
res = float('-inf')
n = len(nums)
for i in range(n):
    mul = 1
    for j in range(i,n):
        mul *= nums[j]
        res = max(res,mul)
print(res)
"""
