class Solution(object):
    def romanToInt(self, s):
        result = 0
        i = 0
        while i < len(s):
            if s[i] == "I":
                if i + 1 < len(s) and s[i+1] == "V":
                    result += 4
                    i += 2
                elif i + 1 < len(s) and s[i+1] == "X":
                    result += 9
                    i += 2
                else:
                    result += 1
                    i += 1
            elif s[i] == "V":
                    result += 5
                    i += 1
            elif s[i] == "X":
                if i + 1 < len(s) and s[i+1] == "L":
                    result += 40
                    i += 2
                elif i + 1 < len(s) and s[i+1] == "C":
                    result += 90
                    i += 2
                else:
                    result += 10
                    i += 1
            elif s[i] == "L":
                result += 50
                i += 1
            elif s[i] == "C":
                if i + 1 < len(s) and s[i+1] == "D":
                    result += 400
                    i += 2
                elif i + 1 < len(s) and s[i+1] == "M":
                    result += 900
                    i += 2
                else:
                    result += 100
                    i += 1
            elif s[i] == "D":
                    result += 500
                    i += 1
            elif s[i] == "M":
                    result += 1000
                    i += 1
        return result