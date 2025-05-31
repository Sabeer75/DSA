class Solution:
    def isValid(self, s: str) -> bool:
        for i in s:
            if '()' in s:
                s = s.replace('()','')

            elif '[]' in s:
                s = s.replace('[]','')

            elif "{}" in s:
                s = s.replace('{}','')

        return s == ""