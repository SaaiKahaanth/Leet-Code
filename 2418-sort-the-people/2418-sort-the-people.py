class Solution(object):
    def sortPeople(self, names, heights):
        dict={}
        
        for i in range(len(names)):
            dict[heights[i]]=names[i]
        heights.sort()
        j=0
        for i in range(len(names)-1,-1,-1):
            names[j]=(str(dict[heights[i]]))
            j+=1
        return names
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        