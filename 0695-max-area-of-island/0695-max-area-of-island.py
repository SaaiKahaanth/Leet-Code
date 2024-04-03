class Solution(object):
    def maxAreaOfIsland(self, grid):
        max_area=0
        global visited
        global row
        row=len(grid)
        global col
        col=len(grid[0])
        visited=[[False for _ in range(col)]for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if not(visited[i][j]) and grid[i][j]==1:
                    area=0
                    area=self.deep_area(area,i,j,grid)
                    if area>max_area:
                        max_area=area
        return max_area
    def deep_area(self,area,i,j,grid):
        
         if i < 0 or i >= row or j < 0 or j >= col or visited[i][j] or grid[i][j] == 0:
            return area
        
         visited[i][j] = True
         area += 1
         area = self.deep_area(area, i + 1, j, grid)
         area = self.deep_area(area, i - 1, j, grid)
         area = self.deep_area(area, i, j + 1, grid)
         area = self.deep_area(area, i, j - 1, grid)

        #  if j+1 <col and grid[i][j+1]==1 :
        #      area+=1
        #      area=self.deep_area(area,i,j+1,grid)
        #      visited[i][j+1]=True
        #  if  i+1 < row and grid[i+1][j]==1:
        #      area+=1
        #      area=self.deep_area(area,i+1,j,grid)
        #      visited[i+1][j]=True
         return area
        
         
        