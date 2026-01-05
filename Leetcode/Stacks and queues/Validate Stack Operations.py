class Solution:
    def validateOp(self, a, b):
        # code here
        stack = []
        l = 0

        for i in b:
            while (not stack or stack[-1] != i) and l < len(a):
                stack.append(a[l])

                l += 1

            if stack[-1] == i:
                stack.pop()

            else:
                return False

        return len(stack) == 0
