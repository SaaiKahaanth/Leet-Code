class Solution(object):
    def mini(self,n1,n2):
        if len(n1)<len(n2):
            return n1
        else:
            return n2
    def maxi(self,n1,n2):
        if len(n2)<len(n1):
            return n1
        else :
            return n2

    def intersect(self, n1, n2):
        n1.sort()
        n2.sort()
        k=[]
        i=0
        j=0
        
        a1=self.mini(n1,n2)
        a2=self.maxi(n1,n2)

        n=len(n1)
        m=len(n2)
        while(i<n and j<m):
            if n1[i]< n2[j]:
                i+=1
            elif n1[i] > n2[j]:
                j+=1
            elif n1[i] == n2[j]:
                k.append(n1[i])
                i+=1
                j+=1
        return k
"""
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        