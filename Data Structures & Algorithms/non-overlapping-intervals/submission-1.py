class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

    
        if not intervals:
            return 0
        
        remove = 0
        intervals.sort()

        end = intervals[0][1]

        for i in range(1,len(intervals)):
            s,e = intervals[i]

            if   s < end : # they overlap
                remove += 1
                # keep the one that ends earliest
                end = min(end,e)
            else:
                end = e
    
        return remove

        #[ (1,10), (1,2), (2,5)]