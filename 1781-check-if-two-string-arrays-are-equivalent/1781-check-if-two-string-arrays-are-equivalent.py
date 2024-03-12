class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        str1 = ''.join(word1)
        str2 = ''.join(word2)
        return str1 == str2        
"""class Solution(object):
    def arrayStringsAreEqual(self, w1, w2):
        print(self.sortadd(w1),self.sortadd(w2))
        if self.sortadd(w1)==self.sortadd(w2):
            return True
        else:
            return False
    def sortadd(self,w):
        
        s=len(w)
        strg=""
        if s>1:
            for i in range(s):
                strg+=str(w[i])
                print(strg)
            return str(strg)
        else:
            return str(w)
        
        
    
"""


       