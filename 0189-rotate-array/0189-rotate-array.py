class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        print(n)
        print(k)
        self.rev(0,n-1,nums)
        self.rev(0,k-1,nums)
        self.rev(k,n-1,nums)
        return nums
    def rev(self,s,e,nums):
        while s<e:
            nums[s],nums[e]=nums[e],nums[s]
            s+=1    
            e-=1
        
        


        
         
        # temp = nums[:k]
        # nums[:k] = []
        # nums[:0] = temp
        # return nums  # Insert elements from temp at the beginning of nums

# class Solution(object):
#     def rotate(self, nums, k):
#         n=len(nums)
#         k=k%n
#         print n
#         print k
#         temp=nums[:k]
#         del nums[:k]
#         for i in range(len(temp)):
#             nums.insert(0, temp[i])
#         # for i in range(k):
#         #     nums.insert(0,nums[n-1])
#         #     nums.pop(n)
#         return nums
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
        