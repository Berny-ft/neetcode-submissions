from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @lru_cache
        def recur(position):
            if position < len(s):
                state = False
                for word in wordDict:
                    if s.find(word,position) == position:
                        state = state or recur(position + len(word))
                
                if not state:
                    return False
                return True
                
            return True
        
        return recur(0)
            
        