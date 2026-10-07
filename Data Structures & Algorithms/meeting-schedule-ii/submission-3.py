"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap = []

        rooms = 0
        intervals.sort(key= lambda x: x.start)

        for meeting in intervals:
            if not heap:
                rooms += 1
            elif heap[0] > meeting.start  :# the earliers finishing meeting 
                rooms += 1
            else:
                heapq.heappop(heap) # we have to pop to fully remove that one form our calendar or sels it will be inaccurate 
            heapq.heappush(heap,meeting.end)
        
        return rooms