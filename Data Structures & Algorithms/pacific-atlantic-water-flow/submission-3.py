class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])

        pac, alt = set(),set()

        def dfs(r,c, visit, previousHeight):
            if (r,c) in visit or r < 0 or c <0 or c == COLS or r == ROWS or heights[r][c] < previousHeight : 
                return
            visit.add((r,c))
            dfs(r+1,c, visit, heights[r][c])
            dfs(r-1,c, visit, heights[r][c])
            dfs(r,c+1, visit, heights[r][c])
            dfs(r,c-1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0,c, pac, heights[0][c]) # we have the current height as the start
            dfs(ROWS - 1, c, alt, heights[ROWS - 1][c] )
            

        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r, COLS-1, alt, heights[r][COLS-1])

        sol = list(pac.intersection(alt))
        return [ [y,x] for y,x in sol ]  


        # so the steps to solving this one are as followed

        # starting form each ocean create a tree by going up in elevation util you can't anymore 
        # the solution will be the itersection of both trees because going down from those nodes allows to reach both oceans
        
        