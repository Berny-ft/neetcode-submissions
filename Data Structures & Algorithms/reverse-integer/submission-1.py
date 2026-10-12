class Solution:
    def reverse(self, x: int) -> int:
        y= x
        # for the interger chekc we'llse see avter
        neg = False
        if x < 0:
            neg =True
            x *= -1
        s=""
        while x >9:
            s += str(x%10)
            x = x//10

        s += str(x%10)

        s = int(s)
        if neg:
            s *= -1
        print(s)

        return s if -2**31 <= s <=  2**(31)- 1 else 0