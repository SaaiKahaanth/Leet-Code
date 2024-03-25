class Solution(object):
    def differenceOfSum(self, nums):
        element_sum=sum(nums)
        digit_sum=0
        for i in nums:
            if i >9:
                while(i!=0):
                    digit=i%10
                    digit_sum+=digit
                    i/=10
            else:
                digit_sum+=i
        return abs(digit_sum-element_sum)

        """
        :type nums: List[int]
        :rtype: int
        """
        