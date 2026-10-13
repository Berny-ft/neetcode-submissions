class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # find overlapping grups 
        # if overlapping gorup is odd remove teh middle element 
        # if they still overlaop remove the middle element until they dont' overlaop 

        #do that for all overlapping groups
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