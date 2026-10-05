class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for i in nums:
            if i not in seen:
                seen.add(i)
            elif i in seen:
                return True
        return False
            