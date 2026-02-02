class Solution:
    def subsetSums(self, arr):
        summ = 0
        ans = []
        self.helper(0, summ, arr, ans)
        return ans

    def helper(self, i, summ, arr, ans):
        if i == len(arr):
            ans.append(summ)
            return

        # include current element
        self.helper(i + 1, summ + arr[i], arr, ans)

        # exclude current element
        self.helper(i + 1, summ, arr, ans)
