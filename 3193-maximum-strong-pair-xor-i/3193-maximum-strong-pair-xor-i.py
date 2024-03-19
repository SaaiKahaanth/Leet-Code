class Solution(object):
    def maximumStrongPairXor(self, nums):
        maxi=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if(abs(nums[i]-nums[j])<=min(nums[i],nums[j])):
                    maxi=max(maxi, nums[i]^nums[j])
        return maxi


        """
        :type nums: List[int]
        :rtype: int
        """
        