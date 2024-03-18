class Solution(object):
    
    def cellsInRange(self, s):
        ans=[]
        a=string.ascii_uppercase
        
        for i in a[a.index(s[0]):a.index(s[3])+1]:
            for j in range(int (s[1]),int(s[4])+1):
                ans.append(str(i+str(j)))
        return ans



        """
        :type s: str
        :rtype: List[str]
        """
        