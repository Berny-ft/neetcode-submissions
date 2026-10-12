class Solution:
    def isPalindrome(self, x: int) -> bool:
        # without converting to string ? 
        #x = str(x)
        #return x == x[::-1]

        # read it forwads and read it backwards
        if x < 0 :
            return False
        arr = []
 
        while x > 9:
            arr.append(x % 10)
            x = math.floor(x // 10)
        arr.append(x)

        return arr == arr[::-1]
            
        