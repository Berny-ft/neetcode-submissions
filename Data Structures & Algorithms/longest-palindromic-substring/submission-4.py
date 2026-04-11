class Solution:
    def longestPalindrome(self, s: str) -> str:
        # so you are given a string you must return le th longest substrinf of s tha tia a lindrom e
        # teh general ideal i woudl have is staring from each point look how much could I expend from here
        # keep track of the longest current then movon to the next letter so that is on2
        # how does this get sovled with dynamic programming 
        # solve the current problem then sovle the nex tone ... 
        # the longerst sumbstring what does this sting add to the longest string we've got already ..??
        # I think my solution is the better one and is actually on2 don't thin kyou can check multiplek pals without doien 
        # on2
        # don't add prints since they reduce the time complexity 

        longest = s[0]
        MIN = 0
        MAX = len(s)-1

        def expand(left,right):
            
            
            while left >= 0 and right <= MAX and s[left] == s[right] :
               
                left -= 1
                right += 1
            
            return s[left+1:right]
            


        
        for i in range(len(s)):
            odd = expand(i,i)
            even = expand(i,i+1)
            
            m  = odd if len(odd) > len(even) else even

            if len(m) > len(longest):
                longest = m
        
        return longest

        
        