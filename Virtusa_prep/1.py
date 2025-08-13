n = int(input())
for i in range(n):
    # 0 1 2 3 4
    if i < n - 1:
        print("#" * (n - 1 - i) + "-" * (i + 1) + "#" * (n - 1 - i))
    else:
        print("-" * (n))
"""  5 lines 
####-#### 
###--### 
##---##
#----#
-----
"""
