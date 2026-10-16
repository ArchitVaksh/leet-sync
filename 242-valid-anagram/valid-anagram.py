class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a = {}
        b = {}

        for ch in s:
            a[ch] = a.get(ch, 0) + 1

        for ch in t:
            b[ch] = b.get(ch, 0) + 1

        return a == b