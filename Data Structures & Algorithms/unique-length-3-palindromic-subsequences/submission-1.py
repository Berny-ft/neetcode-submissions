class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        l = set()


        def expand(i):
            left = set(s[:i])
            right = set(s[i+ 1:])

            for j in left & right: #   pretty cool systanx taht saves you form having to write an iff statement
                l.add((j,s[i],j))
        
        for i in range(len(s)):
            expand(i)
        return len(l)
             
            

         
        

       