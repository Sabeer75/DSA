# Method 1
# merge sort + index return
def merge_sort(nums):
    if len(nums) > 1:
        left_nums = nums[: len(nums) // 2]
        right_nums = nums[len(nums) // 2 :]

        # recursion
        merge_sort(left_nums)
        merge_sort(right_nums)

        # merge
        i = j = k = 0
        while i < len(left_nums) and j < len(right_nums):
            if left_nums[i] < right_nums[j]:
                nums[k] = left_nums[i]
                i += 1
            else:
                nums[k] = right_nums[j]
                j += 1
            k += 1
        # adding the left over values in left and right nums
        while i < len(left_nums):
            nums[k] = left_nums[i]
            i += 1
            k += 1
        while j < len(right_nums):
            nums[k] = right_nums[j]
            j += 1
            k += 1


def findKthLargest(nums, k):
    merge_sort(nums)
    return nums[-k]


nums = [3, 2, 1, 5, 6, 4]
k = 2
print(findKthLargest(nums, k))
"""
nums = [3, 2, 1, 5, 6, 4]
k = 2
nums.sort()
print(nums[len(nums) - k])
"""
