class Solution(object):
    def missingNumber(self, nums):
        maxi=max(nums)
        mini=min(nums)
        for i in range(0,maxi+1):
            if i not in nums:
                return i
        return len(nums)
        """
        :type nums: List[int]
        :rtype: int
        """
        