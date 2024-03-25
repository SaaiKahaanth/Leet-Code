class Solution(object):
    def minOperations(self, nums, k):
        nums=sorted(nums)
        print(nums)
        if k in nums :
            return nums.index(k)
        else:
            c=0
            for j in nums:
                if j<k:
                    c+=1
            return c

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        