class Solution(object):
    def isPalindrome(self, s):
        
        s=s.lower()
        a=""
        for i in s:
            if i.isalnum():
                a+=i
        print a
        if len(a)<=1:
            return True
        else:
            i=0
            j=len(a)-1
            while(i<j ):
                if a[i]!=a[j]:
                    print (i,j)
                    return False
                else:
                    i+=1
                    j-=1
            return True

        
        """
class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        a = ""
        
        for i in s:
            if i.isalnum():  # Check if the character is alphanumeric
                a += i
        
        i = 0
        j = len(a) - 1
        
        while i < j:
            if a[i] != a[j]:
                return False
            else:
                i += 1
                j -= 1
        
        return True
"""
        