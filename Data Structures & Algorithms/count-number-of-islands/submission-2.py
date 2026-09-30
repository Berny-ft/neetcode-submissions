class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # ffind a anlist cooutn it and make sure to eliminate all the surrounding land pieces
        
        # what is my algorithm 
        # row by column . :
            # if you find a land piece: count it
              # run dfs on it until the stack is empty: for each land see et it 0 a water peice
        
        # return the count of the land pieices

        islands = 0

        R = len(grid)
        C = len(grid[0])

        def dfs(grid,i,j):
            nonlocal R,C
            grid[i][j] = "0"
            stack = [(i,j)]
            while stack:
                row, col = stack.pop()
                for drow, dcol in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr, nc = row + drow, col + dcol
                    if 0<= nr < R and 0<= nc< C and grid[nr][nc] == "1":
                        stack.append((nr,nc))
                        grid[nr][nc] = "0"

                



        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == "1" : # we have a land piece
                    islands += 1 
                    dfs(grid,i,j)
                
        return islands
                

        