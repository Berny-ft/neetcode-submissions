class Solution:
    def climbStairs(self, n: int) -> int:
        # so trying to use the dp solution here
        # the idea is that if you are at the last step to there's 1 way to reach the end
        # if you are at the second to last step there are 2 ways 1 step then onone more or 2
        # but if you are at the 3rd to alst then how many steps can you take ? 
        # yu've essentially got 1 + 2 ways to do it since you are given two options to take one or to take 2 afterwards 
        # so the sum of the either one step ahead and two steps ahead will yield the number of steps you can actually take

        one,two = 1,1

        for i in range(n-2,-1,-1):
            temp = one
            one = one + two
            two = temp

        return one 
            


