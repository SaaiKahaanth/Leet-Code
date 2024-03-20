class Solution(object):
    def subtractProductAndSum(self, n):
        sum=0
        mul=1
        while n!=0:
            digit=n%10
            sum+=digit
            mul*=digit
            n=n/10
        return mul-sum

        """
        :type n: int
        :rtype: int
        """
        