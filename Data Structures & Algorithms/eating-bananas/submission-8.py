class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # you coudl sort the piles then what ? 
        # eat k banakes form that bine  
        # so you take your banan pile and what do you do wiht ith ? 
        # for all the piles that are grater than k the time is pile size // k gives you how many houses you need to eat it + 1
        # if the pile is less than k return 1 hr 

        # so you coudl compute teh time by going from 1 to k but # youa re looking for a value 
        # so might as well do binary search 



        def compute(k):
            s = 0
            for i in piles:
                if i <= k:
                    s += 1
                if i > k:
                    s += (i + k - 1) // k
            return s
         

        m = float('inf')

        left = 1
        right = max(piles)
        while left <= right:
            mid = left + (right-left) // 2
            print(mid)
            compute_val = compute(mid)
            if compute_val <= h:
                m = min(m, mid)
                right = mid-1
            else:
                left = mid +1

        return m