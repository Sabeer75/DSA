from collections import defaultdict
s = "ADOBECODEBANC"
t = "ABC"
max_len = float('inf')
t_count = defaultdict(int)
s_count = defaultdict(int)

for ch in t:
    t_count[ch] +=1

l = 0 
for r in range(len(s)):
    if s[r] in t:
        s_count[s[r]] += 1

    if t_count <= s_count:
        max_len = min(max_len,(r-l+1))
        s_count[s[l]] -= 1
        while s[l] in t:
            l += 1
        
print(max_len)


    
