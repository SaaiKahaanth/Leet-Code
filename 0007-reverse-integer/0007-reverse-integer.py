class Solution(object):
    def reverse(self, x):
        rev=0
        o=x
       
       
        if x<0:
            x=-x
        while (x!=0):
            rem=x%10
            rev=rem+rev*10
            x/=10
        if (rev <= -2**31 or rev >= 2**31-1):
            return 0
        if o>0:
            return rev
        else :
            return -rev
            
            
        """
        :type x: int
        :rtype: int
        """
        