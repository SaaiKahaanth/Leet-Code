class Solution(object):
    def twoSum(self, nums, target):
        
        
        idx=[]
        
        for i in range(0,len(nums)):
            
            for j in range(0,len(nums)):
                if((nums[i]+nums[j]==target)and(i!=j)):
                    idx.append(i)
                    idx.append(j)
                    return idx

        
        