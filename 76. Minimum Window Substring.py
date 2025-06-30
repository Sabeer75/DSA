s = "ADOBECODEBANC"
t = "ABC"
if t == "":
    print("")
countT , window = {} , {}

for i in t :
    countT[i] = 1 + countT.get(i,0)

res = [-1,-1]
reslen = float("infinity")
have , need = 0, len(countT)
l = 0 
for r in range(len(s)):
    c = s[r] 
    window[c] = 1 + window.get(c,0)

    if c in countT and window[c] == countT[c]:
        have += 1 
    while have == need:
        if (r-l+1) < reslen:
            res = [l,r]
            reslen = (r-l+1)
        window[s[l]] -= 1 
        if s[l] in countT and window[s[l]] < countT[s[l]]:
            have -= 1
        l += 1
l,r = res 
if reslen != float('infinity'):
    print(s[l:r+1])
else:
    print('')