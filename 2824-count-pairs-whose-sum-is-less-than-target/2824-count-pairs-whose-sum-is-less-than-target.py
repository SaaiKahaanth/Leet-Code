class Solution(object):
    def countPairs(self, nums, target):
        c=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] <target:
                    c+=1
        return c
                
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        