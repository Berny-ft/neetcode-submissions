from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)

        for i in strs:
            sorted_i = "".join(sorted(i))
            m[sorted_i].append(i) # if it doens't exist i creates it and appends 
        return list(m.values())