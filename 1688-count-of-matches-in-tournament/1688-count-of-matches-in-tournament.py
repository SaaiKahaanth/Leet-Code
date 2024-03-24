class Solution(object):
    def fun(self,n ,s):
        if(n==1):
            s+=1
            return s
        elif n %2==0:
            s+=(n / 2)
            return self.fun(n / 2,s)
        else:
            s+=(n - 1) / 2
            return self.fun((n - 1) / 2 + 1,s)


    def numberOfMatches(self, n):
        s=0
        return self.fun(n,s)-1



        


        """
        :type n: int
        :rtype: int
        """
        