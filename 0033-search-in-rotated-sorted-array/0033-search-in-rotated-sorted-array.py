class Solution(object):
    def simplebs(self,n,t,l,r):
        if l>r:
            return -1
        mid=(l+r)//2
        if (n[mid]==t):
            return mid
        if (n[l]<=n[mid]):#Left_sorted
            if (n[l]<=t and n[mid]>=t):
                return self.simplebs(n,t,l,mid-1)
            else:
                return self.simplebs(n,t,mid+1,r)
        else :
            if (n[mid]<=t and t <= n[r]):
                return self.simplebs(n,t,mid+1,r)
            else:
                return self.simplebs(n,t,l,mid-1)




    def search(self, n, t):
        l=0
        r=len(n)-1

        return self.simplebs(n,t,l,r)
    

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        