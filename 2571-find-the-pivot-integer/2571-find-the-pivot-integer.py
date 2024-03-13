class Solution(object):
    def pivotInteger(self, n):
        s=[]
        for i in range(0,n+1):
            s.append(i)
        for i in range(0,n+1):
            if sum(s[:i+1])==sum(s[i:]):
                return i
        return -1
        """
        :type n: int
        :rtype: int
        """
        