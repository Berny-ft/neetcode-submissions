class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return the k most frequent element in the arrya 
        # so you must find their frequency throgh hashing 
        # there is only 1 unique answer so 
        # you want to sort in reverse. so the values sue be tuples with value and count 
        # then return teh value after flipping the rray 

        m = {}
        for i in nums:
            if i  in m:
                m[i] += 1
            else:
                m[i] = 1
        
        l = [(m[i],i) for i in m]
        l.sort(reverse=True)

        sol =[]
        for i in range(k):
            sol.append(l[i][1])
        return sol


        