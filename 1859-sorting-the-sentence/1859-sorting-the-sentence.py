class Solution(object):
    def sortSentence(self, s):
        s+=" "
        n=s.count(" ")+1
        
        
        sample=""
        
        hash={}
        for i in range(len(s)):
            
            if s[i] ==" "  :
                hash[int(s[i-1])]=sample
                sample=""
            elif s[i].isalpha():
                sample+=s[i]
            
        return " ".join(str(hash[i]) for i in range(1,n))




