class Solution(object):
    def findDisappearedNumbers(self, nums):
        ans=[]
        sample=set(nums)
        for i in range(1,len(nums)+1):
            if i not in sample:
                ans.append(i)
        return ans

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        