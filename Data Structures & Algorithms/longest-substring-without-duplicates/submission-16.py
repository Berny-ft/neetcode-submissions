class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:



        longest = 0
        left = 0
        m = set()
        for i,right in enumerate(s):
            if right in m:
                longest = max(longest,len(m))

                while right in m :
                    m.remove(s[left])
                    left +=1
            
            m.add(right)

        if len(m) > longest:
            longest = len(m)

        return longest


        