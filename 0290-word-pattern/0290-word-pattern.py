class Solution(object):
    def wordPattern(self, pattern, s):
        l=[]
        a=""
        for i in s:
            if i!=" ":
                a+=i
            else:
                l.append(a)
                a=""
        l.append(a)
        print l
        if len(pattern)!=len(l):
            return False
        pattern_to_s={}
        s_to_pattern={}
        for i in range(len(pattern)):
            p=pattern[i]
            w=l[i]

            
            if p in pattern_to_s:
                if pattern_to_s[p]!=w:
                    return False
            if w in s_to_pattern:
            
                if s_to_pattern[w]!=p:
                    return False
            
            pattern_to_s[p]=w
            
            s_to_pattern[w]=p
    
        return True





        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        