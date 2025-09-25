nums = [2, 3, 4, 5, 1]

mini = float("inf")
l, r = 0, len(nums) - 1

while l <= r:
    m = (l + r) // 2
    mini = min(mini, nums[m])

    if nums[l] <= nums[m]:
        mini = min(mini, nums[l])
        l = m + 1
    else:
        mini = min(mini, nums[m])
        r = m - 1
print(mini)
