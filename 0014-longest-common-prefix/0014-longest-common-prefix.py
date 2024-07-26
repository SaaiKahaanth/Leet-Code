class Solution:
    def longestCommonPrefix(self, s):
        res=""
        s1=sorted(s)
        strt=s1[0]
        end=s1[len(s)-1]
        for i in range(len(strt)):
            if strt[i]!=end[i]:
                break
            res+=strt[i]
        return res


