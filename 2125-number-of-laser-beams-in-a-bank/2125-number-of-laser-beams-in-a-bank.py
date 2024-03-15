class Solution(object):
    def counti(self,arr):
        l=[]
        for i in arr:
            s=len(i)
            
            c=0
            for j in range(0,s):
                if i[j]=="1":
                    c+=1
                    
            if c!=0:
                l.append(c)
                
            
        return l

    def numberOfBeams(self, bank):
        ans=self.counti(bank)
        n=len(ans)
        s=0
        print n
        
        for i in range(n-1,0,-1):
            t=ans[i]*ans[i-1]
            s=s+t
            print(i,s)
        return s
        """
        :type bank: List[str]
        :rtype: int
        """
        