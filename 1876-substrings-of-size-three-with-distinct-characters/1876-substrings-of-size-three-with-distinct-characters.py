class Solution(object):
    def countGoodSubstrings(self, s):
        count=0
        i=0
        j=2
        while(j<len(s)):
            temp=s[i:j+1]
            print temp
            set=[]
            for x in range (len(temp)):
                c=0
                
                if temp[x] not in set:
                    set.append(temp[x])
                else:
                    c=1
                    break
                
                
            if c==0:
                count+=1
            i+=1
            j+=1
        return count


        """
        :type s: str
        :rtype: int
        """
        