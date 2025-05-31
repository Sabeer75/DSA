def maj(nums):
    nums.sort()
    print(nums)
    count = 0
    for i in nums:
        if nums[i] == nums[i+1]:
            count
        continue
    return nums[len(nums)/2]

nums = [3,3,4,5,6,7,7,7,7,7,7,7,6,6,6,6]
print(maj(nums))