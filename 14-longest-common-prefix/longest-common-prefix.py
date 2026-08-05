class Solution(object):
    def longestCommonPrefix(self, strs):
        result = ""
        index = 0
        while True:
            current = ""
            for word in strs:
                if index >= len(word):
                    return result
                current += word[index]
            flag = True
            for i in range(1, len(current)):
                if current[i] != current[0]:
                    flag = False
                    break
            if flag:
                result += current[0]
                index += 1
            else:
                return result