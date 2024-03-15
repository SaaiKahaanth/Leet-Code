class Solution(object):
    def leftRightDifference(self, a):
        n=len(a)
        ls=[0]*n
        rs=[0]*n
        
        i=1
        j=n-2

        while(i<(n)and j>-1):
            ls[i]=ls[i-1]+a[i-1]
            rs[j]=rs[j+1]+a[j+1]
            i+=1
            j-=1
        for i in range(0,n):
            a[i]=(abs(ls[i]-rs[i]))
        return a

        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        