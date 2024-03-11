class Solution:
    def maxSubArray(self, nums):
        pre = list(nums)

        # Iterate through the list starting from the second element
        for i in range(1, len(nums)):
            pre[i] += max(0, pre[i-1])  # If pre[i-1] is negative, replace it with 0

        return max(pre)  # Find the maximum element in the modified cumulative sum list
