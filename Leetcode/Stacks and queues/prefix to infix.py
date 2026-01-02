class Solution:
    def prefixToInfix(self, s: str) -> str:
        # empty stack
        stack = []

        # iterate backwards and do the pairing
        for i in s[::-1]:
            if i.isalnum():
                stack.append(i)
            else:
                t1 = stack.pop()
                t2 = stack.pop()
                conv = "(" + t1 + i + t2 + ")"
                stack.append(conv)

        return stack[-1] if stack else None
