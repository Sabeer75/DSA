class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0

        while i <= len(s) and s[i] == " ":
            i += 1

        sign = 1
        if i < len(s) and (s[i] == "+" or s[i] == "-"):
            if s[i] == "-":
                sign = -1
            else:
                sign = 1
            i += 1

        return self.helper(s, i, 0, sign)

    def helper(self, s, i, num, sign):
        int_min = -(2**31)
        int_max = 2**31 - 1
        if i == len(s) or not s[i].isdigit():
            return sign * num

        num = num * 10 + int(s[i])

        if sign * num <= int_min:
            return int_min
        elif sign * num >= int_max:
            return int_max

        return self.helper(s, i + 1, num, sign)
