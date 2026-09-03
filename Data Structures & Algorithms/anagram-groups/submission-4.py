class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ok so this shoudl be relatively easy 
        # you need 1 pass wiht hash map : 
        # you store the sorted version of the workd as awell as its unsorted version 
        # if you encounter a sorted new vrsion you keep it in the the value list 
        # so the has map has keys that have for values arrays of anagrams

        h ={}
        for i in strs:
            if "".join(sorted(i)) in h:
                h["".join(sorted(i))].append(i)
            else:
                h["".join(sorted(i))] = [i]
        
        return  [ h[i] for i in h]
