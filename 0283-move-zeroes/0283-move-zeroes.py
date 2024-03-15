class Solution(object):
    
    def moveZeroes(self, a):
        snowball=0
        for i in range(0,len(a)):
            if a[i]==0:
                snowball+=1
            elif(snowball>0):
                t=a[i]
                a[i]=0
                a[i-snowball]=t
        
            
        return a
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        