class SubrectangleQueries(object):

    def __init__(self, rectangle):
        """
        :type rectangle: List[List[int]]
        """
        self.rectangle=rectangle
        

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        for i in range(row1,row2+1):
            for j in range(col1,col2+1):
                self.rectangle[i][j]=newValue
        return None

        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :type newValue: int
        :rtype: None
        """
        

    def getValue(self, row, col):
        return self.rectangle[row][col]

        """
        :type row: int
        :type col: int
        :rtype: int
        """
        


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)