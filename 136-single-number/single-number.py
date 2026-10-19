class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        my_dict = {}

        for i in nums:
            my_dict[i] = my_dict.get(i, 0) + 1

        for key, value in my_dict.items():
            if value == 1:
                return key