from collections import defaultdict
strs = ["eat","tea","tan","ate","nat","bat"]
dic = defaultdict(list)

for word in strs:
    key = [0] * 26
    for char in word:
        key[ord(char) - ord('a')] += 1 
    dic[tuple(key)].append(word) 
print(list(dic.values()))



