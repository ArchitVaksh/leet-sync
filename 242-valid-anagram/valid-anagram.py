class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_count = {}
        t_count = {}
        for i in s:
            if i in s_count:
                s_count[(i)] += 1
            elif i not in s_count:
                s_count[(i)] = 1
        for j in t:
            if j in t_count:
                t_count[(j)] += 1
            elif j not in t_count:
                t_count[(j)] = 1
        if s_count == t_count:
            return True
        else:
            return False