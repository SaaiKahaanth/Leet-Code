class Solution(object):
    def maxProduct(self, nums):
        max1=max(nums)
        nums.remove(max1)

        max2=max(nums)
        nums.remove(max2)

        return (max1 -1)*(max2-1)
        """
        :type nums: List[int]
        :rtype: int
        """
        