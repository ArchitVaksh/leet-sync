class Solution(object):
    def findMissingElements(self, nums):
        nums.sort()
        first = nums[0]
        last = nums[-1]
        result = []
        for i in range(first,last+1):
            if i not in nums:
                result.append(i)
        return result