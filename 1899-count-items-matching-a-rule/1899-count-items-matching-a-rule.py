class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        l=["type","color","name"]
        ind=l.index(ruleKey)
        c=0
        for i in range(len(items)):
            if items[i][ind]==ruleValue:
                c+=1
        return c
        
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        