class Solution:
    def findLucky(self, arr: List[int]) -> int:
        if not arr: 
            return -1

        m = {}

        for i in arr:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1

        print(m)

        maxx = -1
        for i in m:
            if m[i] == i:
                maxx = max(maxx, i)
        
        return maxx
        