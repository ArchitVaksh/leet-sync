class Solution(object):
    def isPalindrome(self, s):
        left = 0
        right = len(s)-1
        while left <= right:
            if not s[left].lower().isalnum():
                left += 1
            elif not s[right].lower().isalnum():
                right -= 1
            else:
                if s[right].lower() != s[left].lower():
                    return False
                else:
                    right -= 1
                    left += 1
        return True

