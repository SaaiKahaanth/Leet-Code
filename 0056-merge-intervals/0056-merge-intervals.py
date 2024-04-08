class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        merged = []
        for i in range(len(intervals)):
            if not merged or merged[-1][1] < intervals[i][0]:
                merged.append(intervals[i])
            else:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
        return merged


# class Solution(object):
#     def merge(self, intervals):
#         intervals.sort()
#         merged=[]
#         for i in range (len(intervals)):
#             if merged==[]:
#                 merged.append(intervals[i])
#             else:
#                 previous_end=merged[-1][0]
#                 current_start=intervals[i][0]
#                 current_end=intervals[i][1]
#                 if previous_end>=current_start:
#                     merged[-1][1]=max(previous_end,current_end)
#                 else:
#                     merged.append(intervals[i])
#         return merged

#         """
#         :type intervals: List[List[int]]
#         :rtype: List[List[int]]
#         """
        