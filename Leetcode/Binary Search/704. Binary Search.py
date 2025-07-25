nums = [-1, 0, 3, 5, 9, 12]
target = 9
l, r = 0, len(nums) - 1
while l <= r:
    m = (l + r) // 2
    if nums[m] == target:
        print(m)
        break
    elif nums[m] < target:
        l = m + 1
    else:
        r = m - 1
else:
    print("-1")
