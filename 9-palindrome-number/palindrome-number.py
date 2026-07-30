class Solution(object):
    def isPalindrome(self, x):
        a = x
        if a < 0:
            return False
        n = int(str(a)[ : :-1])
        if n == x:
            return True
        else:
            return False
