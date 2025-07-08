s = "abcab"
n = len(s)
lps = [0] * n
j = 0
i = 1
while i < n:
    if s[i] == s[j]:
        j += 1
        lps[i] = j
        i += 1
    else:
        if j != 0:
            j = lps[j-1]
        else:
            lps[i] = 0
            i += 1
print(len(s[:lps[-1]]))


"""s = "abcab"
n = len(s)

print("All prefixes:")
for i in range(1, n): 
    prefix = ""
    for j in range(i):
        prefix += s[j]
    print(prefix)

print("\nAll suffixes:")
for i in range(1, n): 
    suffix = ""
    for j in range(n - i, n):
        suffix += s[j]
    print(suffix)
"""

''' my code 
from collections import defaultdict
s = "aaaa"
l_dict = defaultdict(int)
r_dict = defaultdict(int)
final = []
l = 0
r = len(s) - 1
if len(s) % 2 != 0:
    middle = len(s) // 2
    while l< middle and r > middle:
        l_dict[s[l]] += 1 
        r_dict[s[r]] += 1
        final.append(s[l])
        if l_dict == r_dict:
            print(final)
        l += 1 
        r -= 1
else:
    while l <= r:
        l_dict[s[l]] += 1 
        r_dict[s[r]] += 1
        final.append(s[l])
        if l_dict == r_dict:
            print(final)
        l += 1 
        r -= 1
        
'''