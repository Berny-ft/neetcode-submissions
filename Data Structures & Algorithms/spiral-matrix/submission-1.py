class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        """ this is a graph problem 
        you shoudl be going left as mushc as possible if not go donw 
        if no go right if not go up 

        """
        sol = []
        states = [ (0,1), (1,0),(0,-1),(-1,0)]
        state = 0
        start = [0,0]
        R = len(matrix)-1
        C = len(matrix[0])-1
        sol.append(matrix[start[0]][start[1]])
        matrix[start[0]][start[1]] = None
        while True:
            

            row = start[0]+states[state][0]
            col = start[1]+states[state][1]
            while 0 <= row <= R and 0 <=  col <= C and  matrix[row][col] is not None:

                sol.append(matrix[row][col])
                matrix[row][col] = None
                start = [ start[0]+states[state][0] , start[1]+states[state][1]]
                row = start[0]+states[state][0]
                col = start[1]+states[state][1]
            
            state = (state+1)%4
            if len(sol) == (R+1) * (C+1):
                break

        return sol 
        