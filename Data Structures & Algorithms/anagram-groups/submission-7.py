class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        table = defaultdict(list)

        for i in strs:

            key = "".join(sorted(i))

            table[key].append(i)

        sol =[]

        for i in table:
            sol.append(table[i])

        return sol