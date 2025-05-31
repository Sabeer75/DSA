def findValidPair(s):
        d = {'1': 0, '2': 0,'3': 0,'4':0, '5':0,'6':0, '7': 0, '8':0, '9': 0}

        for i in s:
              d[i] += 1
        
        for i in range(len(s)-1):
               if s[i] != s[i+1]:
                      if d[s[i]] == int(s[i]) and d[s[i+1]] == int(s[i+1]):
                             return s[i] + s[i+1]
s = '2523533'
print(findValidPair(s))
