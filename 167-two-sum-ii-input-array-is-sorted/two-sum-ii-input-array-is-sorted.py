class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers)-1
        while i <= len(numbers)-1 and j >= 0:
            if (numbers[i]+numbers[j]) > target:
                j -= 1
            elif (numbers[i]+numbers[j]) < target:
                i += 1
            else:
                my_string = [i+1,j+1]
                return my_string