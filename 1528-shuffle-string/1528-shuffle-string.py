class Solution(object):
    def restoreString(self, s, indices):
        n=len(s)
        ans=[0]*n
        for i in range(n):
            ans[indices[i]]=s[i]
        return "".join(ans)

        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """