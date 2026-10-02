import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # each grid locaiton shoudl hold the number of ways to get to it 
        ''' the final gird position has 2 ways to get to it 
        down or right. so then i go to the location righ tabove i know that the location right obove and the quetion to ask here is does this how di i get here ? well coming donr from dwon is the same path so no new aditions .  there' probably a sta wya to get this in o(1)
        we are essentailly counting the amount of times we can swtich from down to rihght or right to down within the grid. nothign comes to midn immediately 


        so then what you should do is have a queue to which you psush adjacents nodes once you'e pushed adnajce nodes 
        you compare then to the sender if the rtanstion was donw or right we add nothign to the golobal counter in such a way we are checking all checking everywhere . so then then on the next round . acutally for each star node you shoudl fully hanlde it bfore going to anothe rnode in the que what about a node that is snee twice well it alrady has teh number of wasy we get to it if you get it again nd its coming fom a difernt direciton you add to the count 

        

        dp=  [[0]*n for x in range(m)]
        dp[m-1][n-1] = 2

        print(dp)

        q = deque((m-1,n-1))

        while q:


            row,col = q.popleft()

            coords = [(-1,0),(0,-1)]
            for r,c in coords:
                if 0 <= row+r  and 0 <= col :
                    q.append((row+r, col+c))

                    if row+r == row: 
                        # same direction so the numbers of way to reach this location doesnt' increase
                        dp[row+r][col+c]= dp[row][col]
                    else: #this means you changed oclumns 
                        dp[row+r][col+c]= dp[row][col] + 1
        '''


        return math.comb(m + n - 2, m - 1)




                        


        
        