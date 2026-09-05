import heapq
class Solution:
    def topKFrequent(self, nums,k):
        res = []
        freq = {}

        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0) + 1 

        arr = [[] for _ in range(len(nums) + 1)]
        for num , count in freq.items():
            arr[count].append(num) 

        for j in range(len(arr)-1,0,-1):
            for l in arr[j]:
                res.append(l)
                if len(res) == k:
                    return res 