class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        if len(arr) < k:
            return ""

        l = []

        # i have to find all distr
        m = {}
        
        for i in arr:
            if i not in m:
                m[i] = 1
            elif m[i] > 1:
                continue
            else:
                m[i] += 1
        
        for i in m:
            if m[i] == 1:
                l.append(i)
        
        if len(l) < k:
            return ""
        return l[k-1]
        