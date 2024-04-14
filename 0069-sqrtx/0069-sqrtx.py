class Solution(object):
    def mySqrt(self, x):
        res=0
        if x==0:
            return 0
        if x==1:
            return 1


        l,r=0,x
        while l<=r:
            m=l+((r-l)//2)


            if m**2<x:
                l=m+1
                res=m
                

                
            elif m**2>x:
                r=m-1
                 
            else:
                return m
        
        return res
        """
        :type x: int
        :rtype: int
        """
        