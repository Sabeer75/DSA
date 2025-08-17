nums = [3, 4, 5, 1, 2]
mini = float("inf")
l, r = 0, len(nums) - 1
while l <= r:
    mid = (l + r) // 2

    mini = min(nums[mid], mini)

    if nums[l] <= nums[mid]:
        mini = min(nums[l], mini)
        l = mid + 1
    else:
        mini = min(nums[mid], mini)
        r = mid - 1

print(mini)
