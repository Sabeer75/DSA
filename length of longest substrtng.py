def lengthOfLongestSubstring(s) -> int:
    final_length = 0
    substr = ''
    for i in range(len(s)):
        
        if s[i] not in substr:
            substr=substr+s[i]
        else:
            final_length = max(final_length,len(substr))
            print(substr)
            substr = substr[substr.index(s[i])+1:]+ s[i]
            print(substr)
    return max(final_length,len(substr))

s = 'abcbaed'
print(lengthOfLongestSubstring(s))