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

        start = 0
        end = len(s)-1

        while start <= end:
            if s[start] != s[end]:
                return False
            else:
                start += 1
                end -=1
        return True
        