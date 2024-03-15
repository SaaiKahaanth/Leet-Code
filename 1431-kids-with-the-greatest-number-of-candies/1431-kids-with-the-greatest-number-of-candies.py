class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        
        maxi=max(candies)
        print(maxi)
        for i in range(0,len(candies)):
            
            candies[i]+=extraCandies
            
            if candies[i]>=maxi:
                candies[i]=1
            else:
                candies[i]=0
           
        return candies
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        