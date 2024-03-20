class Solution(object):
    def smallestEvenMultiple(self, n):
        i=n
        while (i<=15000):
            if i%2==0 and i%n==0:
                return i
            if i%2==0:
                i+=2
            else:
                i+=1    
            
        return -1
        """
        :type n: int
        :rtype: int
        """
        