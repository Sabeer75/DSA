class Solution:
    def maxLength(self, s):
        # code here
        maxi = 0

        open = close = 0

        l = 0
        r = len(s) - 1

        openf = closef = 0
        openb = closeb = 0

        while l <= len(s) - 1 and r >= 0:
            if s[l] == "(":
                openf += 1
            else:
                closef += 1

            if openf == closef:
                maxi = max(maxi, 2 * closef)

            elif closef > openf:
                closef = openf = 0

            if s[r] == "(":
                openb += 1
            else:
                closeb += 1

            if openb == closeb:
                maxi = max(maxi, 2 * openb)

            elif closeb < openb:
                closeb = openb = 0

            l += 1
            r -= 1

        return maxi
