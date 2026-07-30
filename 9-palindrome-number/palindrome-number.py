class Solution(object):
    def isPalindrome(self, x):
        n = str(x)[ : :-1]
        if n == str(x) and x >= 0:
            return True
        else:
            return False