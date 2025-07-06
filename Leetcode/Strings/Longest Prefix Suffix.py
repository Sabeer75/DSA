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

    
        
            




