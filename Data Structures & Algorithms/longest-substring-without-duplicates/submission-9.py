class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # you need a substring without repreating so its a sliding window problem 
        left = 0
        window = set()
        max_len = 0

        for right in range(len(s)):
            if s[right] not in window:
                window.add(s[right])
                max_len = max(max_len,len(window))
            else:
                while s[right] in window:
                    window.remove(s[left])
                    left +=1
                    
                window.add(s[right]) # changed one char for another we cannot have a new max len
        
        return max_len

        