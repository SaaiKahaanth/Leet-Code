class Solution(object):
    def insert(self, intervals, newInterval):
        ans=[]
        start,end=newInterval[0],newInterval[1]
        right,left=[],[]
        for i in intervals:
            if i[1]<start:
                left.append(i)
            elif i[0]>end:
                right.append(i)
            else:
                start=min(start ,i[0])
                end=max(end,i[1])
        ans.append(left)
        ans.append([start,end])
        ans.append(right)
        return left+[[start,end]]+right

            
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        