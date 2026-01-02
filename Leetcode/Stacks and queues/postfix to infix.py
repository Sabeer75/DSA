class Solution:
    def post_to_infix(self, post_exp: str) -> str:
        # an empty stack
        stack = []

        for i in post_exp:
            # if numbers or alphabets append instack
            if i.isalnum():
                stack.append(i)
            # else take the above 2 characters from stack
            # and the oprator in between and wrap it up with brackets
            else:
                t2 = stack.pop()
                t1 = stack.pop()
                conv = "(" + t1 + i + t2 + ")"
                stack.append(conv)

        return stack[-1]
