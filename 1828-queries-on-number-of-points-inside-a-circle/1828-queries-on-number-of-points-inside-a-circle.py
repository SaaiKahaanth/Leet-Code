class Solution(object):
    def countPoints(self, points, queries):
        
        ans=[]
        for q in range (len(queries)):
            c=0
            for p in range (len(points)):
                a=((((queries[q][0]-points[p][0])**2)+((queries[q][1]-points[p][1])**2))**0.5)
                if(a<=queries[q][2]):
                    c+=1
                a=0
            ans.append(c)
        return ans
                    
                
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        