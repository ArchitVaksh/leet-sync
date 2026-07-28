class Solution(object):
    def firstUniqChar(self, s):
        target = 0

        while target < len(s):
            current = 0

            while current < len(s):
                if target != current and s[target] == s[current]:
                    break
                current += 1

            if current == len(s):
                return target

            target += 1

        return -1