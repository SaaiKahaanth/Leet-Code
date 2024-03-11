class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen =set ()
        maximum_length = 0
        start = 0
        end = 0
        while end < len (s):
            if s[end] not in seen :
                seen.add(s[end])
                end +=1
                maximum_length = max(maximum_length, len (seen))
            else:
                seen.remove(s[start])
                start += 1
        return maximum_length