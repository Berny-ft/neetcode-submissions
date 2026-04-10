class Solution:
    def rob(self, nums: List[int]) -> int:
        # do still have to really get a good understanding of it the idea makes sense. more practice tho
        rob1, rob2 = 0,0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2
        