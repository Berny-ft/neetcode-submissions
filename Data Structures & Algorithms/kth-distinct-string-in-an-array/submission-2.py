from collections import OrderedDict
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        m = OrderedDict()
        for i in arr:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1
        
        counter = 0
        for i in m:
            if m[i] == 1:
                counter += 1
                if counter ==k:
                    return i
        
        return ""

            