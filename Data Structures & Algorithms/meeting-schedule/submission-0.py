"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # if meetings overlaop return false
        if not intervals:
            return True
        intervals = sorted(intervals,key=lambda x: x.start)

        intervals = deque(intervals)

        end = intervals.popleft().end


        while intervals:
            node = intervals.popleft()
            s,e = node.start,node.end
            if  s < end:
                return False
            end = e

        return True 
