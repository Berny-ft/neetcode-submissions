class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        good_orange_count = 0
        bad_orange_locations = deque()
        for i,row in enumerate(grid):
            for j, location in enumerate(row):
                if location == 1:
                    good_orange_count += 1
                elif location == 2:
                    bad_orange_locations.append((i,j))

        R,C = len(grid), len(grid[0])

        minutes = 0
        
        while bad_orange_locations:
            round_contaminations = 0

            for _ in range(len(bad_orange_locations)):
                row, col = bad_orange_locations.popleft()
                grid[row][col] = 0

                coords = [ (0,1), (0,-1), (-1,0), (1,0)]
                for i,j in coords:
                    if 0 <= row +i < R and 0 <= col +j < C and grid[row+i][col+j] == 1:
                        # we have to contamniate this lcoation 
                        bad_orange_locations.append( (row+i, col+j))
                        grid[row+i][col+j] = 2
                        good_orange_count -= 1
                        round_contaminations += 1

                
            if round_contaminations:
                minutes += 1
        
        if not good_orange_count:
            return minutes
        return -1

        