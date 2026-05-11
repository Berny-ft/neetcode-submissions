class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # decide at each stage where you have an open or a close parenthese

        sol = []
        o = n
        c = n

        #" we cna only add a close if the count of close is less than the open count"

        def recur(o , c , curr):
            if o == 0  and c == 0:
                sol.append(curr) 
                return 
            
            # we do 2 branches one where we close and the other where we dont 
            if o > 0:
                recur(o - 1, c, curr + "(" ) 

            if c > o :
                
                recur(o, c - 1 , curr + ")") 
            
        
        recur(n,n, "")

        return sol
           
           


               