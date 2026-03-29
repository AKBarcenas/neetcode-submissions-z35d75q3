"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 1:
            return True

        intervals.sort(key=lambda i: i.start)
        for index in range(len(intervals) - 1):
            if intervals[index].end > intervals[index + 1].start:
                return False 

        return True