class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        longest = 1

        for i in nums:
            if i-1 in nums:
                continue
            
            value = i
            length = 1
            while value + 1 in nums:
                length += 1
                value = value + 1
            longest = max(longest,length)

        return longest
        