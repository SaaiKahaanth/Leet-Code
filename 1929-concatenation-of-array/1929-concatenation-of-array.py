class Solution(object):
    def getConcatenation(self, nums):
        l=[]
        i=0 
        j=0
        n=len(nums)
        while(i<n):
            l.append(nums[i])
            i=i+1
            if i>=n and j==0:
                i=0
                j=1
        return l
                
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        