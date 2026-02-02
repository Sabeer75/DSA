class Solution:
    def combinationSum(self, candidates, target):

        ans = []
        ds = []
        self.find_combination(0, target, candidates, ans, ds)
        return ans

    def find_combination(self, index, target, candidates, ans, ds):
        if index == len(candidates):
            if target == 0:
                ans.append(list(ds))
            return

        if candidates[index] <= target:
            ds.append(candidates[index])
            self.find_combination(
                index, target - candidates[index], candidates, ans, ds
            )
            ds.pop()

        self.find_combination(index + 1, target, candidates, ans, ds)
