s = "ABABBA"
k = 2

count = {}
max_len = 0 
l = 0 

for r in range(len(s)):
    count[s[r]] = 1 + count.get(s[r],0)
    frequent = max(count.values())

    if (r - l + 1) - frequent > k:
        count[s[l]] -= 1
        l += 1 

    max_len = max(r - l + 1 , max_len)
print(max_len)