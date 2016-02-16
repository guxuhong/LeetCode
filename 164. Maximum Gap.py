"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
Try to solve it in linear time/space.
Return 0 if the array contains less than 2 elements.
You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
"""

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        maxnum = max(nums)
        minnum = min(nums)
        bucketrange = max(1, int((maxnum - minnum - 1) / (n - 1)) + 1)
        bucketlength = (maxnum - minnum) / bucketrange + 1
        buckets = [None] * bucketlength
        for num in nums:
            position = (num - minnum) / bucketrange
            bucket = buckets[position]
            if bucket == None:
                bucket = [num, num]
                buckets[position] = bucket
            else:
                bucket[0] = min(bucket[0], num)
                bucket[1] = max(bucket[1], num)
        maxgap = i = 0
        while i < bucketlength:
            if buckets[i] == None:
                i += 1
                continue
            j = i + 1
            while j < bucketlength and buckets[j] == None:
                j += 1
            if j < bucketlength:
                maxgap = max(maxgap, buckets[j][0] - buckets[i][1])
            i = j
        return maxgap
