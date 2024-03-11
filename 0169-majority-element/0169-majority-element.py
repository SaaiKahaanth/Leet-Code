class Solution(object):
    def majorityElement(self, nums):
        m=0
        uniq=[]
        for i in nums:
            if i not in uniq :
                uniq.append(i)
        for i in range (len(uniq)):
            
            if m< nums.count(uniq[i]):
                c=0
                m=(nums.count(uniq[i]))
                c=uniq[i]
        return c
                
            
        """
        :type nums: List[int]
        :rtype: int
        """
        