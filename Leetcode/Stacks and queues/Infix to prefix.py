class Solution:
    # define priority
    def prec(self, c):
        if c == "^":
            return 3
        elif c == "*" or c == "/":
            return 2
        elif c == "+" or c == "-":
            return 1
        else:
            return -1

    def infix_to_prefix(self, infix: str) -> str:
        # Your code goes here
        stack = []
        res = []
        # for infix to prefix
        # 1. rev the infix
        rev = infix[::-1]

        rev = rev.replace("(", "#")
        rev = rev.replace(")", "(")
        rev = rev.replace("#", ")")

        # dont handle the same operator precedence and perform infix to postfix
        for c in rev:
            if c.isalnum():
                res.append(c)
            elif c == "(":
                stack.append("(")
            elif c == ")":
                while stack and stack[-1] != "(":
                    res.append(stack.pop())
                if stack:
                    stack.pop()
            else:
                while (
                    stack and stack[-1] != "(" and self.prec(c) < self.prec(stack[-1])
                ):
                    res.append(stack.pop())
                stack.append(c)

        while stack:
            res.append(stack.pop())
        # reverse the output got after changing infix to postfix
        res.reverse()

        return "".join(res)
