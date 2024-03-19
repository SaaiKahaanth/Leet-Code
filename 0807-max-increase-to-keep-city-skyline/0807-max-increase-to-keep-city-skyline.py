class Solution(object):
    def maxelement(self,grid,x,y):
        tempmax=[]
        for i in range(x):
            max=0
            for j in range(y):
                if grid[i][j]>max:
                    max=grid[i][j]
            tempmax.append(max)
        return tempmax

    def maxIncreaseKeepingSkyline(self, grid):
        row=len(grid)
        col=len(grid[0])
        
        rowmax=self.maxelement(grid,row,col)
        
        transposed_grid = [[grid[j][i] for j in range(row)] for i in range(col)]
        colmax = self.maxelement(transposed_grid, col, row)
        print (rowmax,colmax)
        sum=0
        for i in range(row):
            for j in range(col):
                sum+=min(rowmax[i],colmax[j])-grid[i][j]
        return sum


        
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        