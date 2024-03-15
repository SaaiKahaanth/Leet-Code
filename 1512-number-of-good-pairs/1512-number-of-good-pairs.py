class Solution(object):
    def numIdenticalPairs(self, nums):
        n=len(nums)
        c=0
        for i in range(0,n-1):
            for j in range (i+1,n):
                if nums[i]==nums[j]:
                    c+=1
        return c
        """
        :type nums: List[int]
        :rtype: int
        """
        