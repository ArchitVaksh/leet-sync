class Solution(object):
    def addDigits(self, num):
#leet-sync
        def sum_of_digits(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit
                num //= 10
            return total

        while num >= 10:
            num = sum_of_digits(num)

        return num      