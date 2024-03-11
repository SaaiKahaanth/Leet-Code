class Solution(object):
    def maxProfit(self, p):
        l=0
        r=1
        max_p=0
        while(r<len(p)):
            if (p[r]>p[l]):
                max_p=max((p[r]-p[l]),max_p)
            else:
                l=r
            r+=1
        return max_p