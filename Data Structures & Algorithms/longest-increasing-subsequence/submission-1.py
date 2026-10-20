class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        from the end position you integrate the current digit 
        you define the longest subsequence you've been able to get at this point 
        which ends up being just a single digit 
        you then go backwars to teh previous state . at this point what is the longest you can get 
        it is either the logest subsequence including the next digigit if the next digit is greater than the current one 
        or else its just this one 
        --- well actually in this position would you have to iterate to the end to find if there is any bigger valeu than the current that woudl represnet the start of a valid subsquence ? maybe seems plausible becuse the following digit only would necessarilpy tell a story about all the potnetual subs sequences following up . 
        so the time complexity 
        so you do 1 pass  N for each element in  you do up to a maximum of. an extra pass to find if there is a subsquence thatis taccheable to it. 

        actually you do have to go the end because you coudl find a gibeer number cool that is big bu tthen later you could find a value that is a bit smaller than the one you just found bu tsitll bether and has potenti to create a longer subsquence 

        so time compelxity is On^2
    
        '''
        
        n = len(nums)

        if n <= 1:
            return n
        dp = [0] * n 
        print(dp)
        dp[n-1] = 1

        overall_max = 1
        for i in range(len(nums)-2,-1,-1):
            
            current = nums[i]
            max_here = 1 # the current value 
            for j in range(i+1, n):
                if nums[j] > current:

                    max_here = max(max_here, 1+ dp[j] )
            
            dp[i] = max_here

            overall_max = max(overall_max, max_here)
            

        return overall_max

                
            































        