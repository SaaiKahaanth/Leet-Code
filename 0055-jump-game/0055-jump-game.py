class Solution(object):
    def canJump(self, nums):
        goal=nums[len(nums)-1]

        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>= goal:
                goal =i
        return True if goal==0 else False 
        """
        :type nums: List[int]
        :rtype: bool
        """
        