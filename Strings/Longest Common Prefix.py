def Longest_Common_Prefix(strs):
    a = " "
    strs.sort()
    first = strs[0]
    last = strs[-1]
    for i in range(len(first)):
        if first[i] == last[i]:
            a += first[i]
        else:
            break 
    return a 


strs = ["dog","racecar","car"]
print(Longest_Common_Prefix(strs))