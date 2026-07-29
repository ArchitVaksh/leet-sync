class Solution(object):
    def twoSum(self, nums, target):
        result = []
        a = 1

        for number in nums:
            for i in range(a, len(nums)):
                if nums[i] + number == target:
                    result.append(a - 1)
                    result.append(i)
                    return result
            a += 1