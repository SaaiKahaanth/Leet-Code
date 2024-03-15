class Solution(object):
    def buildArray(self, nums):
        l=[]
        for i in range (0,len(nums)):
            l.append(nums[nums[i]])
        return l
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        