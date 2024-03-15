class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        s=0
        for i in range(len(nums)):
            c=0
            b=str(bin(i))
            c=b.count("1")
            if c==k:
                s+=nums[i]
        return s
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        