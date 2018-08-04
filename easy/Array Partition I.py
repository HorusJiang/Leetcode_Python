class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort()
        # i = 0
        # sum = 0
        # while i < len(nums):
        #     sum += nums[i]
        #     i += 2
        # return sum
        return sum(sorted(nums)[::2])
        