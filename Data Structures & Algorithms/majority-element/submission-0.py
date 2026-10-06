from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        for i in count:
            if count[i] > math.floor(len(nums)/2):
                return i