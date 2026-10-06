class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


        '''
        so the grid represnets all the oranges
        we shoudl first find all the rotten oranges locations
        find all the good oragens count 

        then staring a all the rotten oranges location we all push tem into a queue
        for the number of rotten oranges in that queue 
        add all the neighbouring good aranges we can catch  as we mark a good orange as rotten we change its value to empty so that the if a another orange was adject to it it doenst get added twice . 
        each cycle we count howmany new good ranges we've foudn and rotten by. if at the end of teh cule we compare the number of good orange at the start and the end if it is the same count then that means we havnet found any new good arnage to corumpt and if that value isgreater than 0 that means we cna't reach all of them if the number of good oranges ever reaches 0 that means we reached all of them . we must count the number of loop iterations snice eahc loop iteration tells us  the number of mintes spent on that orange.

        '''

        good = 0
        bad = deque([])
        for i,row in enumerate(grid):
            for j,orange in enumerate(row):
                if orange == 1: 
                    good += 1
                elif orange == 2:
                    bad.append((i,j))

        

        minutes = 0
        R = len(grid)-1
        C = len(grid[0])-1

        while bad:
            good_start = good
            for i in range(len(bad)):
                x,y = bad.popleft()
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nx,ny = x+dx,y+dy
                    if 0<= nx <= R and 0<= ny <= C and grid[nx][ny] == 1:
                        grid[nx][ny] = 0
                        bad.append((nx,ny))
                        good -= 1
            
            if good == good_start:
                break
            if good == 0:
                minutes += 1
                break
            minutes += 1

        if good > 0:
            return  -1
        return minutes


                








