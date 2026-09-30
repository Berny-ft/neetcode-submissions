class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # you need a substring without repreating so its a sliding window problem 
        left = 0
        window = set()
        max_len = 0

        for right, char in enumerate(s):
            while char in window: 
                window.remove(s[left])
                left += 1
            window.add(char)
            max_len = max(len(window), max_len)
        return max_len

        