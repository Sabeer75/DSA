class Solution:
    def reversePairs(self, nums):
        count = 0 
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr)//2

            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            check(left,right)

            return merge(left,right)

        def check(left,right):
            nonlocal count
            i = 0 
            j = 0 
            while i < len(left) and j < len(right):
                if left[i] > 2 * right[j]:
                    count += len(left)-i
                    j += 1 
                else:
                    i += 1

        def merge(left,right):
            res = []

            i = 0 
            j = 0 
            while i<len(left) and j<len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1 
                else:
                    res.append(right[j])
                    j += 1 
            while i < len(left):
                res.append(left[i])
                i += 1 
            while j < len(right):
                res.append(right[j])
                j += 1 

            return res 

        merge_sort(nums)
        return count 