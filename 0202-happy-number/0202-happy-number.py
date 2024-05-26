class Solution(object):
    def isHappy(self, n):
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            sum_of_squares = 0
            while n > 0:
                digit = n % 10
                sum_of_squares += digit * digit
                n //= 10
            n = sum_of_squares
        return n == 1

# # Example usage:
# sol = Solution()
# print(sol.isHappy(19))  # Output: True
