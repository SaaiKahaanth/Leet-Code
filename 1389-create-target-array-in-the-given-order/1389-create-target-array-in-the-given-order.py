class Solution(object):
    def createTargetArray(self, nums, index):
        """n=len(nums)
        res=[]
        for i in range(0,n):
            if index[i]<i:

                res.insert(index[i],nums[i]) 
            else:
                res.append(nums[i])

            
        return res
        """
        arr = []
        for n,i in zip(nums,index): 
            arr[i:i] = [n]
        return arr