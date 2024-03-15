class Solution(object):
    def finalValueAfterOperations(self, operations):
        X=0
        for i in range (0,len(operations)):
            if (operations[i] == "--X")or(operations[i]=="X--"):
                X=X-1
            else :
                X=X+1

        return X
    
        """
        :type operations: List[str]
        :rtype: int
        """
        