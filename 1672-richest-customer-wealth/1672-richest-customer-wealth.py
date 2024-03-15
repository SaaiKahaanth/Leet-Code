class Solution(object):
    def maximumWealth(self, accounts):
        n=len(accounts)
        maxi=0
        sum=0
        
        for i in range (0,n):
            sum=0
            for j in range (0,len(accounts[i])):
                sum+=accounts[i][j]
            maxi=(max(maxi,sum))
        return maxi
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        