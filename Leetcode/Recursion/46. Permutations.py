class Solution:
    def permute(self, nums):
        res = []
        def bt(ds,used):
            if len(ds) == len(nums):
                res.append(ds.copy())
                return 
            for i in range(len(nums)):
                if used[i]:
                    continue 

                used[i] = True 
                ds.append(nums[i])

                bt(ds,used)

                ds.pop()
                used[i] = False

        bt([],[False]*len(nums))

        return res 