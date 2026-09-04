class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # this is a set problem as well as two pointers
        #you start with both poitners on the fist character you move the front frowards. if you encounter the same character you popleft until that character is gone then you restart adding from the right . you must pop ultil the characeter is gone on the left the right 
        

        if len(s) <= 1:
            return len(s)

        left = 0
        right = 1


        longest = s[0]
        sol = longest

        for i,val in enumerate(s):
            if val not in longest:
                longest += val
                if len(longest) > len(sol):
                    sol = longest
            else:

                while val in longest:
                    longest = longest[1:]


                longest += val

        return len(sol)

