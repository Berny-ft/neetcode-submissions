class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # you could use a hashmap to store the frequency of each elemetn and then sort the list based on the frequency and return the top k elemnts 
        # you could also use a heap to store the frequency of each element and then sort the list based on the frequency and return the top k... 
        # pretty sure this is a heap problme what could you push 

        m = {}
        for i in nums: 
            if i not in m: 
                m[i] = (i,1)
            else:
                key,count = m[i]
                m[i] = (key, count+1)

        values = sorted( m.values(), key=lambda pair: pair[1] ,reverse=True  )
        values = [x for x,y in values]
        return values[:k]