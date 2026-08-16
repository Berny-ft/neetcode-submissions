class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs: 
            return []

        m = {}
        
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in m:
                m[sorted_s] = [s]
            else:
                m[sorted_s].append(s)
        
        return list(m.values())
        