def isPalindrome(s):
        s = list(s.lower())
        ss = []
        for i in s:
            if i.isalnum():
                ss.append(i)
        return ss == ss[::-1]






    

