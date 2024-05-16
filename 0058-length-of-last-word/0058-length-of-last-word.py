class Solution(object):
    def lengthOfLastWord(self, s):
        n=len(s)
        c=0
        for i in range(n-1,-1,-1):
            if s[i]!=" ":
                c+=1
                
            elif c>=1 and s[i]==" ":
                return c
        return c
                


        """
        :type s: str
        :rtype: int
        """
        