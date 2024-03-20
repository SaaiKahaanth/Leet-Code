class Solution(object):
    def differenceOfSums(self, n, m):
        sum_m,sum_n=0,0
        for i in range(1,n+1):
            if i%m!=0:
                sum_m+=i
                print sum_m
            if i%m==0:
                sum_n+=i
                print sum_n
        return sum_m-sum_n
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        