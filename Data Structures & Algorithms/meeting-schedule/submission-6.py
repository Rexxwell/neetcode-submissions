"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    # Brute Force
    # Runtime: 48ms
    # Memory: 8.0 MB
    # Time Complexity: O(n^2)
    # Memory: O(1)
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i in range(len(intervals)):
            interval1 = intervals[i]
            for j in range(i+1, len(intervals)):
                interval2 = intervals[j]
                # If meeting 1 starts before meeting 2 ends and meeting 1 ends after meeting 2 starts,
                # then there is a conflict.
                # If we changed it to a or instead of an end, then there will be an edge case where
                # meeting 1 will start before meeting 2 ends but meeting 1 ends before meeting 2 starts.
                if (interval1.start < interval2.end and interval1.end > interval2.start):
                    return False
        return True
