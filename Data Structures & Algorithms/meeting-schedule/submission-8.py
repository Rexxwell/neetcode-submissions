"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # Sorting Approach
    # Runtime: 45ms
    # Memory: 8.0 MB
    # Time Complexity: O(nlogn)
    # Space Complexity: O(n)
    #   .sort() uses Timsort, which is a mix of merge sort and insertion sort
    #   merge sort uses O(n/2) = O(n) space to do the merging.
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval: interval.start) # O(nlogn)
        for i in range(len(intervals) - 1):
            interval1 = intervals[i]
            interval2 = intervals[i+1]
            if (interval1.start < interval2.end and interval1.end > interval2.start):
                return False
        return True