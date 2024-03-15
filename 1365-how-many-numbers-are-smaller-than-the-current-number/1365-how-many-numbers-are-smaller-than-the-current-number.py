class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        c=[]
        for i in range (len(nums)):
            co=0
            for j in range (len(nums)):
                if nums[i]>nums[j]:
                    co+=1
            c.append(co)
        return c
               
                
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        