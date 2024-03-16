class Solution(object):
    def balancedStringSplit(self, s):
        sumi,c=0,0
        for i in s:
            if i=="R":
                sumi+=1
            elif i=="L":
                sumi-=1
            if sumi==0:
                c+=1
        return c

        """
        :type s: str
        :rtype: int
        """
        