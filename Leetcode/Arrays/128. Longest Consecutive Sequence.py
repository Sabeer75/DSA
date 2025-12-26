class Solution:
    def longestConsecutive(nums) -> int:
        nums.sort()
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1

        maxi = 1
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == 1 + nums[i - 1]:
                count += 1
            elif nums[i] == nums[i - 1]:
                continue
            else:
                count = 1
            maxi = max(maxi, count)
        return maxi
