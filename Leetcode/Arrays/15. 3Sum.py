nums = [-1, 0, 1, 2, -1, -4]
nums.sort()
print(nums)
res = []

for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    else:
        target = -nums[i]
        l, r = i + 1, len(nums) - 1

        while l < r:
            two_sum = nums[l] + nums[r]
            if two_sum == target:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r += 1

"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                two_sum = nums[left] + nums[right]
                if two_sum == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicate second and third elements
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif two_sum < target:
                    left += 1
                else:
                    right -= 1

        return res
"""
