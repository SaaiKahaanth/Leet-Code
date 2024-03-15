class Solution(object):
    def shuffle(self, nums, n):
        s=[]
        for i in range(0,n):
            s.append(nums[i])
            s.append(nums[n+i])
        return s
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        