class Solution(object):
    def maxProfit(self, s):
        lowest = s[0]
        profit = 0
        max_profit = 0
        for i in range(0,len(s)):
            current = s[i]
            if current < lowest:
                lowest = current
            profit = current - lowest
            if profit > max_profit:
                max_profit = profit
        return max_profit