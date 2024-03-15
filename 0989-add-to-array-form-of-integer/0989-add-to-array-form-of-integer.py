class Solution(object):
    def addToArrayForm(self, num, k):
        sum=0
        for i in range(0,len(num)):
            digit=sum*10
            sum=num[i]+digit
        res=str(k+sum)
        ans=[0]*len(res)
        for i in range (len(res)):
            ans[i]=int(res[i])


        
        return ans

        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        