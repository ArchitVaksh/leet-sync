class Solution(object):
    def longestCommonPrefix(self, strs):
        result = ""
        index = 0
        while True:
            if index >= len(strs[0]):
                return result
            first = strs[0][index]
            for word in strs[1:]:
                if index >= len(word):
                    return result
                if word[index] != first:
                    return result
            result += first
            index += 1