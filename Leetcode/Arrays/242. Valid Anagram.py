class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=  len(t):
            return False
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        l = 0 
        r = 0 
        while l< len(sorted_s) and r < len(sorted_t):
            if sorted_t[r] != sorted_s[l]:
                return False 
                break
            l += 1
            r += 1 

        else:
            return True
        