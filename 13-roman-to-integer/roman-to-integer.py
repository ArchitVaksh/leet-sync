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
        while i > 0:
            if romans[s[i]] > romans[s[i-1]]:
                result += romans[s[i]]
                result -= romans[s[i-1]]
                i -= 2
            else:
                result += romans[s[i]]
                i -= 1
        if i == 0:
            result += romans[s[i]]
        return result