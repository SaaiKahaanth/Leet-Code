class Solution(object):
    def maxProductDifference(self, nums):
        #FIRST MIX
        mini1=min(nums)
        nums.remove(mini1)

        #SECOND MIX
        mini2=min(nums)
        nums.remove(mini2)
        
        #FIRST MAX
        maxi1=max(nums)
        nums.remove(maxi1)

        #SECOND MAX
        maxi2=max(nums)
        nums.remove(maxi2)
        
        #Maximum Product Difference Between Two Pairs
        return((maxi1*maxi2)-(mini1*mini2))

        """
        :type nums: List[int]
        :rtype: int
        """