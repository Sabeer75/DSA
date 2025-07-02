s = "abcde"
res_words = []

for i in range(len(s)):
    l,r = i,i
    while l >= 0 and r < len(s) and s[l] == s[r]:
        res_words.append(s[l:r+1])
        l -= 1
        r += 1 
    
    l,r = i, i+1
    while l >= 0 and r < len(s) and s[l] == s[r]:
        res_words.append(s[l:r+1])
        l -= 1
        r += 1
print(len(res_words))