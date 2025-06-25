from collections import defaultdict 
s = "geeksforgeeks"
count = defaultdict(int)

for i in s:
    count[i] += 1

for x in count:
    if count[x] > 1:
        print([x,count[x]], end = ",")





