class Solution(object):
    def sortedSquares(self, nums):
        for i in range(len(nums)):
            nums[i]=abs(nums[i]*nums[i])
        return sorted(nums)
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        