class Solution(object):
    def pivotIndex(self, nums):
         total=sum(nums)
         lsum=0
         for i in range (len(nums)):
              rsum=total-lsum-nums[i]
              if (rsum==lsum):
                   return i
              lsum+=nums[i]
         return -1

