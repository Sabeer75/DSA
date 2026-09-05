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

'''
best 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set(nums)

        longest = 0
        for i in arr:
            if i-1 not in arr:
                count = 1 
                x = i 

                while x+1 in arr:
                    count += 1 
                    x +=1 
                longest = max(longest,count)

        return longest 
'''
