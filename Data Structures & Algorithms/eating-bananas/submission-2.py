class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = right

        while left <= right:
            mid = left + (right -left ) // 2

            total_hours = sum(( p + mid - 1) // mid for p in piles)

            if total_hours <= h:
                ans = mid
                right = mid -1

            else: 
                left = mid +1
        
        return ans