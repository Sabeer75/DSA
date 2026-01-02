class Solution:
    def prefixToPostfix(self, s: str) -> str:
        # Your code goes here
        stack = []

        for i in s[::-1]:
            if i.isalnum():
                stack.append(i)
            else:
                t1 = stack.pop()
                t2 = stack.pop()
                conv = t1 + t2 + i

                stack.append(conv)
        return stack[-1] if stack else None
