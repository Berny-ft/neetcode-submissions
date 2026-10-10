class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:


        '''
        sorting the intervals by start time 
        then waht ? 

        so we sort them by start first then 
        we chekc for the current interval if it ends before the start of the next oen if so we are good mwe move on to the nex toen 
        if it doesnt well we merge them 

        the merge is we take the min fof the start and and hte amx of the ends 

        an we return 1 
        and the merge becomes the curren tinterval 

        so then how do ou stare it 
        ou problaboy shoudl have a array solution to which you push the ine wintervals rather than doing it in palc e


        so heres' the algo 
        sol = []
        while intervals we pop lthem instead it maes it simpment 
            if  next one within range and the next ones start is less or equal to this ones end 
                merge pop hte next one and merge if o push one 




        '''


        intervals.sort()
        intervals = deque(intervals)

        sol = []
        while intervals:
            start,end = intervals.popleft()

            while intervals and intervals[0][0] <= end:
                next_start,next_end =  intervals.popleft()
                end = max(end,next_end)
            
            sol.append([start,end])
        
        return sol

        