class Solution:
    def countSubstrings(self, s: str) -> int:



        MAX = len(s)-1

        count = 0

        def expand(left,right):
            nonlocal count
            
            
            while left >= 0 and right <= MAX and s[left] == s[right] :
               
                left -= 1
                right += 1
                count += 1
            
            
            


        
        for i in range(len(s)):
            expand(i,i)
            expand(i,i+1)
        
        return count
        