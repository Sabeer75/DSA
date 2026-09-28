class Solution:
    def romanToInt(s):
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        pairs = {"I": ['V','X'],"X": ['L','C'], "C": ['D','M']}

        count = 0 

        i = 0 

        while i < len(s):
            if i + 1 < len(s) and s[i] in pairs and s[i+1] in pairs[s[i]]:
                count += roman[s[i + 1]] - roman[s[i]]
                i +=  2
            else:
                count += roman[s[i]]
                i += 1

        return count 
