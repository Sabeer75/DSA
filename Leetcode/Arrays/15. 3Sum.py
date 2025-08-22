nums = [-2, -1, 1, 4, 5, 7, 1]
nums.sort()
res = []
n = len(nums)
for i in range(n):
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    else:
        l, r = i + 1, n - 1
        target = -nums[i]

        while l < r:
            two_sum = nums[l] + nums[r]
            if two_sum == target:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1

                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1

            elif two_sum < target:
                l += 1

            else:
                r -= 1
print(res)


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
