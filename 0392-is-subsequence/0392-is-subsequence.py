class Solution(object):
    def isSubsequence(self, s, t):
        i=0
        j=0
        if(s==t):
            print("1st if")
            return True
        elif(s==""):
            print("2nd if")
            return True

        else:
            while((i<len(s)and j<len(t))):
            

                if s[i]==t[j]:
                
                    i+=1
                    j+=1
                    print(i,j,"seconf if EQUAL")
                
                elif s[i]!=t[j]:
                    j+=1
                    print(i,j,"third ifNOT EQUAL")
                if i==len(s):
                    print(i,j,"first if CONDITION FINISHED")
                    return True
            return False 
        
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        