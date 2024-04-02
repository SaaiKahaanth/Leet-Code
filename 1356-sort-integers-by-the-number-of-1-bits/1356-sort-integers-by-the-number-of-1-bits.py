class Solution(object):
    
    def sortByBits(self, arr):
        arr.sort()
        ans=[]
        dict=defaultdict(list)
        for i in arr:
            dict[str(bin(i)).count(str(1))].append(i)
        listi= sorted(item for sublist in dict.values() for item in sublist)
        print dict
        for i in (dict.values()):
            for item in i:
                ans.append(item)
            # print i
            # ans+= (str(dict[i]))
             
            #  ans.append(i)
            # ans.append(j)for j in temp
            #  for j in temp:
            #     ans+=str(j)
            #  ans+= str([j for j in temp])

        return ans

        """
        :type arr: List[int]
        :rtype: List[int]
        """
        