from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        anagram_map=defaultdict(list)
        res=[]
        for s in strs:
            sorted_s= tuple(sorted(s))
            anagram_map[sorted_s].append(s)
        for value in anagram_map.values():
            res.append(value)
        return res
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        