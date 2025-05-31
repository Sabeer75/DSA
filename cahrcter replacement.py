def cr(s,k):
    count = {}
    l = 0 
    length = 0 

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r],0)
        frequent = max(count.values())
        if (r - l + 1) - frequent >k:
            count[s[l]] -= 1
            l += 1
            
        length = max(r - l +1,length)
    return length
s = "ABABBA"
k = 2
print(cr(s,k))