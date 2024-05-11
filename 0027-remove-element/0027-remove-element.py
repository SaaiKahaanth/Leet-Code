class Solution(object):
    def removeElement(self, nums, val):
        pointer=0
        n=len(nums)
        for i in range(0,n):
            if nums[i]!=val:
                nums[pointer]=nums[i]
                pointer+=1
        return pointer
        

        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        