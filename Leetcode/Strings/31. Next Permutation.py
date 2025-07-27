nums = [1, 2, 3]
for i in range(len(nums) - 2, -1, -1):
    if nums[i] < nums[i + 1]:
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[j], nums[i] = nums[i], nums[j]
        sortit = nums[i + 1 :]
        sortit.sort()
        nums[i + 1 :] = sortit
        break
else:
    nums.sort()
print(nums)
