class Solution(object):
    def thirdMax(self, nums):
        a=sorted(nums)
        l=[]
        for i in a:
            if i not in l:
                l.append(i)
        if len(l)<3:
            return max(l)
        else:
                return( l[len(l)-3])

       
       