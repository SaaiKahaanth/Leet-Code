class Solution(object):
    def findMatrix(self, nums):
        dicts=defaultdict(list)
        sets=[]
        for i in nums:
            if i not in sets:
                for j in range(nums.count(i)):
                    dicts[j].append(i)

                sets.append(i)
        return dicts.values()
                 
                
