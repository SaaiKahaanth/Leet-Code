class Solution(object):
    def isPalindrome(self, x):
        xi=str(x)
        if xi==xi[::-1]:
            return 1

        else:
            return 0
        """
        :type x: int
        :rtype: bool
        """
        