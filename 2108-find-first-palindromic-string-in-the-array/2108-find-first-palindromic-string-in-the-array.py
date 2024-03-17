class Solution(object):
    def firstPalindrome(self, words):
        #100% EFFICIENCY 
        for word in words:
            if word == word[::-1]:
                return word
        return ""
        """
        #MY SOLUTION(WITH 50% CONCIOUSNESS)
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
               
            
        return """

        """
        :type words: List[str]
        :rtype: str
        """
        