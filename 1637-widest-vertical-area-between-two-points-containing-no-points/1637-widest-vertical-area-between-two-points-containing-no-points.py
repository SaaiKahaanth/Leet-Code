class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        points.sort()
        n=len(points)
        x=0
        for i in range (0,n-1):
            x=max(x,(points[i+1][0]-points[i][0]))
        return x
        """
        :type points: List[List[int]]
        :rtype: int
        """
        