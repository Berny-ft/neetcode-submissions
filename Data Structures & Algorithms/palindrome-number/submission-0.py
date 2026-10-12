class Solution:
    def isPalindrome(self, x: int) -> bool:
        # without converting to string ? 
        x = str(x)
        return x == x[::-1]
        