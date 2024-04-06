class Solution(object):
    def deleteGreatestValue(self, grid):
        maxof,ans=0,0
        n=len(grid)
        if len(grid[0])==1:
            return grid[0][0]
        for i in range(len(grid[0])-1):
            for j in range (n):

                max1=max(grid[j])
                grid[j].remove(max1)
                maxof=max(max1,maxof)
            ans+=maxof
        return ans
            
        
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        