
class Solution(object):
    def minOperations(self, boxes):
        ans=[0]*len(boxes)
        lcount,lcost,rcount,rcost,n=0,0,0,0,len(boxes)
        
        for i in range(1,n):
            if boxes[i-1]=="1":
                lcount+=1
            lcost+=lcount
            ans[i]=lcost
        for j in range(n-2,-1,-1):
            if boxes[j+1]=="1":
                rcount+=1
            rcost+=rcount
            ans[j]+=rcost
        

        return ans   
"""
"""
"""
        #bruteforce time taken @first trial 14:05 miniutes 
        n=len(boxes)
        res=[]
        for i in range(n):
            op=0
            for j in range(n):
                if boxes[j]=="1":
                    op+=abs(j-i)
            res.append(op)
        return res
        """
"""
        :type boxes: str
        :rtype: List[int]
        """
        