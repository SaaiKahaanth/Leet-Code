class Solution(object):
    def generate(self, numRows):
        a=[]
        a.append([1])
        if numRows>1:
            a.append([1,1])
        i=2
        while i<numRows:
            a.append([0]*(i+1))
            a[i][0],a[i][i]=1,1
            k=0
            for j in range(1,i):
                a[i][j]=a[i-1][k]+a[i-1][k+1]
                k+=1
            i+=1
        return a
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        