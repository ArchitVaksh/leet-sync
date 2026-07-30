class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        n = int(str(x)[ : :-1])
        if n == x:
            return True
        else:
            return False