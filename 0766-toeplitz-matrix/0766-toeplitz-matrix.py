class Solution(object):
    def isToeplitzMatrix(self, matrix):
        n=1
        while(n<len(matrix)):
            
            for i in range(len(matrix[0])-1):
                if matrix[n-1][i]!=matrix[n][i+1]:
                    return False
            n+=1
        return True
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        