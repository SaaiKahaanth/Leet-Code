class Solution(object):
    def findWordsContaining(self, words, x):
        a=[]
        for i in range (0,len(words)):
            if x in (words[i]) :
                a.append(i)
        return a
                
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        