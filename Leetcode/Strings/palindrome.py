def isPalindrome(s):
        s = list(s.lower())
        ss = []
        for i in s:
            if i.isalnum():
                ss.append(i)
        return ss == ss[::-1]


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))





    

