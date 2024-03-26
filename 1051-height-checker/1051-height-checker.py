class Solution(object):
    def heightChecker(self, heights):
        expected=sorted(heights)
        c=0
        for i in range(len(expected)):
            if expected[i]!=heights[i]:
                c+=1
        return c
        """
        :type heights: List[int]
        :rtype: int
        """
        