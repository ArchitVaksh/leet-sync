class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = 0
        i = 0
        while j <= len(nums)-2 and i <= len(nums)-1:
            if nums[j] == 0 and nums[i] != 0:
                nums[j],nums[i] = nums[i],nums[j]
                j += 1
                i += 1
            elif nums[i] == 0 and nums[j] == 0:
                i += 1
            else:
                j += 1
                i += 1