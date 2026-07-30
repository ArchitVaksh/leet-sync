class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        reversed_word = ""
        i = len(s)-1
        while i >=0:
            if s[i] != " ":
                reversed_word += s[i]
            elif s[i] == " " and len(reversed_word)!=0:
                break
            i -= 1
        return len(reversed_word)