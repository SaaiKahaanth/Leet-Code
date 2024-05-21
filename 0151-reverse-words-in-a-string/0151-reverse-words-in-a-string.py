class Solution(object):
    def reverseWords(self, s):
        n=len(s)
        i=0
        result=""
        while(i<n):
            while(i<n and s[i]==" "):i+=1
            if i>=n:
                break
            
            j=i+1
            while(j<n and s[j]!=" "):j+=1
            sub=s[i:j]
            if len(result)==0:result=sub
            else:result=sub+" "+result
            i=j+1
        return result
        """
        :type s: str
        :rtype: str
        """
        