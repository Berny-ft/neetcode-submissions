class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # locate all teh os 
        # create a visited set 
        # create list of groupppings
        # go through all. the unvisited 0s if theyy are on the border visited and no grouppring
          # could be more effiient to see if has connection and just remove them as well but  makes the work more difficult 
          # actually # no we should have a state variable for the exploration that allows us to invalidate a gruppping 
          # so we put the entire grouppping in visited without considering them for surrounded propperty

        # go through all the valid grouppings for each node for check if all its borders .... no you can just flip them straight away 
        # since the invalid groupings actually invalidate all the bad ones so just flip them all 
        # wwe shoudl only keep track of the invalid locations and flip everything else 

        ROWS = len(board) - 1
        COLS = len(board[0]) - 1

        locations = set()
        for y,row in enumerate(board):
            for x, val in enumerate(row):
                if val == 'O':
                    locations.add((y,x))

        
        invalid = set()
        visited = set()

        def dfs(row, col, group):
            if row > ROWS or row < 0 or col < 0 or col > COLS or board[row][col] == 'X' or (row, col) in visited:
                return group

            visited.add((row, col))
            group.add((row, col))

            dfs(row-1, col, group)
            dfs(row+1, col, group)
            dfs(row, col-1, group)
            dfs(row, col+1, group)

            return group
                



        for y,x in locations:
            if (y,x) in visited:
                continue
            s = dfs(y,x,set())
            for y,x in s:
                if y == 0 or y == ROWS or x == 0 or x == COLS:
                    invalid = invalid.union(s)
                    break

            
        flippable = locations - invalid

        for y,x in flippable:
            board[y][x] = 'X'
        