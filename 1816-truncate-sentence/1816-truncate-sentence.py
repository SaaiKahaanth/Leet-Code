class Solution(object):
    def truncateSentence(self, s, k):
        c=0
        s=s+" "
        for i in range(len(s)):
            if s[i]==" ":
                c+=1
            if c==k:
                return s[:i]
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        