class Solution(object):
    def groupThePeople(self, groupSizes):
        n=len(groupSizes)
        assing=set()
        group=[]
        res=[]
        for i in range(0,n):
            if i not in assing:
                group=[i]
            
                for j in range(i+1,n):
                
                    if groupSizes[i]==groupSizes[j] and len(group)<groupSizes[i]:
                        group.append(j)
                        assing.add(j)
                res.append(group)   
                                    

                    
                    
               
            
            

        return res
                
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        