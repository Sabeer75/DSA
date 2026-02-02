class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = []
        ds = []
        self.find(0, candidates, target, ans, ds)
        return ans

    def find(self, ind, candidates, target, ans, ds):
        if target == 0:
            ans.append(list(ds))
            return

        for i in range(ind, len(candidates)):
            if i > ind and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break

            ds.append(candidates[i])
            self.find(i + 1, candidates, target - candidates[i], ans, ds)
            ds.pop()
