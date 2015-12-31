"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.
Example 1:
 Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9]. 
Example 2:
 Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16]. 
This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10]. 
Subscribe to see which companies asked this question
"""

"""
我的解法，代码略长
"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        startconfirmed, endconfirmed, ans = False, False, []
        for interval in intervals:
            if endconfirmed:
                ans.append(Interval(interval.start, interval.end))
                continue
            if not startconfirmed:
                if newInterval.start <= interval.start or (interval.start < newInterval.start <= interval.end):
                    newInterval.start = min(newInterval.start, interval.start)
                    startconfirmed = True
            if not endconfirmed:
                if newInterval.end < interval.start:
                    endconfirmed = True
                elif interval.start <= newInterval.end <= interval.end:
                    newInterval.end = interval.end
                    endconfirmed = True
            if not startconfirmed and not endconfirmed:
                ans.append(Interval(interval.start, interval.end))
            if endconfirmed:
                ans.append(Interval(newInterval.start, newInterval.end))
                if newInterval.end < interval.start:
                    ans.append(Interval(interval.start, interval.end))
        if not endconfirmed:
            ans.append(Interval(newInterval.start, newInterval.end))
        return ans


"""
大神实例精简版代码
"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        intervals.sort(key = lambda x : x.start)
        length = len(intervals)
        res = []
        for i in range(length):
            if res == []:
                res.append(intervals[i])
            else:
                size = len(res)
                if res[size-1].start <= intervals[i].start <= res[size-1].end:
                    res[size-1].end = max(intervals[i].end, res[size-1].end)
                else:
                    res.append(intervals[i])
        return res
