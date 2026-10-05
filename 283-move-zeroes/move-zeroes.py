class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        i = 0
        while i <= len(nums)-1:
            if nums[i] == 0:
                nums.remove(nums[i])
                i -= 1
                count += 1
            i += 1
        for countTimes in range(count):
            nums.append(0)