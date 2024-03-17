class Solution(object):
    def firstPalindrome(self, words):
        for i in words:
            s=0
            e=len(i)-1
            while s<=e:
                if i[s]!=i[e]:
                    break
                s+=1
                e-=1
            else:
                return i
               
            
        return ""

        """
        :type words: List[str]
        :rtype: str
        """
        