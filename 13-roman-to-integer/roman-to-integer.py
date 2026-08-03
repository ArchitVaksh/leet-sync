class Solution(object):
    def romanToInt(self, s):
        result = 0
        i = len(s)-1
        romans = {"I":1,
              "V":5,
              "X":10,
              "L":50,
              "C":100,
              "D":500,
              "M":1000}
        for i in range(len(s)):
            if  i+1 < len(s) and romans[s[i]] < romans[s[i+1]]:
                result -= romans[s[i]]
            else:
                result += romans[s[i]]
        return result