class Solution(object):
    def maxArea(self, height):
        max_vol=0
        l=0
        
        r=len(height)-1

        while (l<r ):
            cur_vol=min(height[l],height[r])*(r-l)
            max_vol=max(max_vol,cur_vol)
            if height[l]<height[r]:
                l+=1
            else :
                r-=1
        return max_vol

        """
        :type height: List[int]
        :rtype: int
        """
        