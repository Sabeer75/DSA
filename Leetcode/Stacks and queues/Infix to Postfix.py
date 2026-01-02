class Solution:
    def prec(self, c):
        if c == "^":
            return 3
        elif c == "*" or c == "/":
            return 2
        elif c == "+" or c == "-":
            return 1
        else:
            return -1

    def infixtoPostfix(self, s):
        stack = []
        res = []

        for c in s:
            if c.isalnum():
                res.append(c)
            elif c == "(":
                stack.append("(")
            elif c == ")":
                while stack and stack[-1] != "(":
                    res.append(stack.pop())
                stack.pop()
            else:
                while (
                    stack
                    and stack[-1] != "("
                    and (
                        self.prec(c) < self.prec(stack[-1])
                        or (self.prec(c) == self.prec(stack[-1]) and c != "^")
                    )
                ):
                    res.append(stack.pop())
                stack.append(c)

        while stack:
            res.append(stack.pop())

        return "".join(res)
