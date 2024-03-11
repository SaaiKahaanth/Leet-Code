class Solution(object):
    def combinationSum(self, num , target):
        ret=[]
        self.dfs(num,target,[],ret)
        return ret
    def dfs(self,num,t,path,ret):
        if t<0:
            return
        elif t==0:
            ret.append(path)
            return 
        for i in range(len(num)):
            self.dfs(num[i: ],t-num[i],path+[num[i]],ret)

        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        