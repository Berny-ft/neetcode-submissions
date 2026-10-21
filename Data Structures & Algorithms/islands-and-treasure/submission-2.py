class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        R = len(grid)
        C = len(grid[0])

        for i,row in enumerate(grid):
            for j,col in enumerate(row):
                if col == 0:
                    q.append((i,j))

        
        while q:
            for i in range(len(q)):
                x,y = q.popleft()

                for dx,dy in [(0,1),(0,-1),(-1,0),(1,0)]:
                    nx,ny = dx+x, dy+y
                    if 0<= nx < R and 0 <= ny < C and grid[nx][ny] == 2147483647:
                        grid[nx][ny] = grid[x][y] + 1
                        q.append((nx,ny))

            
        return 




