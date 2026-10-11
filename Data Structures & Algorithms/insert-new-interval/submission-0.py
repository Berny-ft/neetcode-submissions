class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = deque(intervals)

        ns, ne = newInterval
        res = []

        while intervals:
            s,e = intervals.popleft()
            if e< ns:
                res.append([s,e])
            elif s> ne:
                res.append([ns,ne])
                res.append([s,e])
                return res + list(intervals)
            else:
                ns, ne = min(ns,s), max(ne,e)
        res.append([ns,ne])
        return res
        