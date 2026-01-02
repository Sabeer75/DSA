class Solution:
    def postToPre(self, postfix: str) -> str:
        # Your code goes here
        stack = []

        for i in postfix:
            if i.isalnum():
                stack.append(i)
            else:
                t1 = stack.pop()
                t2 = stack.pop()

                conv = i + t2 + t1
                stack.append(conv)
        return stack[-1] if stack else None
