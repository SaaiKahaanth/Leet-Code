class Solution(object):
    def plusOne(self, digits):
        s=""
        for i in digits:
            s=s+str(i)
        digits=[]
        
        ans=str(int(s)+1)
        for i in range(0,len(ans)):
            digits.append(int(ans[i]))
        return digits
        
        
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        