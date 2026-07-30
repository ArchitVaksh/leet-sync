class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        nen = x
        new_digit = ""
        while nen > 0:
            digit = nen%10
            new_digit  += str(digit)
            nen //= 10
        if new_digit == str(x) or x == 0:
            return True
        else:
            return False
