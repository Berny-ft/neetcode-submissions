class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            # check every row 
            l = set()
            for e in row:
                if e == '.':
                    continue
                if e not in l:
                    l.add(e)
                else:
                    return False
            
        
        for i in range(9): # i represents colums
            l = set()
            for j in range(9): # j represents rows
                val = board[j][i]
                if val == '.'  or val ==",":
                    continue
                if val not in l:
                    l.add(val)
                else:
                    return False
            

             
        # Check every 3x3 subgrid
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                l = set()
                for dr in range(3):
                    for dc in range(3):
                        val = board[r + dr][c + dc]
                        if val == "." or val == ",":
                            continue
                        if val in l:
                            return False
                        l.add(val)

            
        return True
                
                
                



        