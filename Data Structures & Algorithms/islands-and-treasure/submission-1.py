class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        

        queue = deque([])
        for i,row in enumerate(grid):
            for j,value in enumerate(row):
                if value == 0:
                    queue.append( (i,j) )

        
        R = len(grid)-1
        C = len(grid[0])-1

        count = 1
        while queue:
            
            for i in range(len(queue)):
                x,y = queue.popleft()
                for nx,ny in [ (0,1), (0,-1), (1,0), (-1,0)]:
                    if 0 <= nx+x <= R and 0 <= ny+y <= C and grid[nx+x][ny+y] == 2147483647 :
                        queue.append( (nx+x,ny+y) )
                        grid[nx+x][ny+y] = count
            
            count += 1
                    

        
                        
