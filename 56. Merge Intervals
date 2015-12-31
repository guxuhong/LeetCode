"""
Given a collection of intervals, merge all overlapping intervals.
For example,
 Given [1,3],[2,6],[8,10],[15,18],
 return [1,6],[8,10],[15,18]. 
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key = lambda x:x.start)
        ans = []
        for interval in intervals:
            if ans == []:
                ans.append(interval)
            else:
                if ans[-1].start <= interval.start <= ans[-1].end:
                    ans[-1].end = max(ans[-1].end, interval.end)
                else:
                    ans.append(interval)
        return ans
