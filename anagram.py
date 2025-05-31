class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s= s.lower()
        t= t.lower()
        ss = list(s)
        tt = list(t)
        
        ss.sort()
        tt.sort()

        return ss == tt