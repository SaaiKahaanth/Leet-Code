class Solution(object):
    def countKDifference(self, nums, k):
        c=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if abs(nums[i]-nums[j])==k:
                    c+=1
        return c

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        