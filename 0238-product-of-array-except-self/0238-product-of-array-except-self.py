class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n  # Initialize ans with all 1s

        # Calculate the product of elements to the left of each index
        left_product = 1
        for i in range(n):
            ans[i] *= left_product
            left_product *= nums[i]

        # Calculate the product of elements to the right of each index
        right_product = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= right_product
            right_product *= nums[i]

        return ans
