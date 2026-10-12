class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=lambda x:len(x))
        print(strs)
        prefix = ""
        for i,letter in enumerate(strs[0]):
            for string in strs:
                if string[i] != letter:
                    return prefix
            
            prefix += letter
        
        return prefix
        