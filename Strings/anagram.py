def isAnagram(s,t):
    s = list(sorted(s))
    t = list(sorted(t))
    return s[0::] == t[0::]  


s = "anagram", t = "nagaram"
print(isAnagram(s,t))
