class Solution(object):
    def numberGame(self, nu):
        n=len(nu)
        
        nu.sort()
        i=0
        while(i<n):
            t=nu[i]
            nu[i]=nu[i+1]
            nu[i+1]=t
            i+=2
           
        return nu
        """
        for i in range(0,len(nums)):
            if len(nums)==0:
                break
            a=min(nums)
            nums.pop(nums.index(a))
            
            b=min(nums)
            nums.pop(nums.index(b))
            
            r.append(b)
            r.append(a)
        return(r)
        """
      
        