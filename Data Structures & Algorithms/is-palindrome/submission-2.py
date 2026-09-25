class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lower case and remove special charactoers
        s = s.lower().replace(' ','')
        test = "qwertyuiopasdfghjklzxcvbnm1234567890"
        for l in s:
            if l not in test:
                s = s.replace(l,'')
                print(l,s)
        print(s)

        return s == s[::-1]

        