class Solution(object):
    def containsDuplicate(self, nums):
        s={}
        for i in nums:
            if i in s and s[i]>=1:
                return 1
            s[i]=s.get(i,0)+1
           
        return 0
        """
        :type nums: List[int]
        :rtype: bool
        """
        