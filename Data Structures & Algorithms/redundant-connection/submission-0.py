class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        sol = [ ]

        # we make an adjecency list and we explore using dfs and you keep track of the nodes that have already been seen 
        # after that if you find a second path to a node that has aredy been visited you can flg that path as being the wrong path 

        h = {}

        # this list can now be explored
        for left,right in edges:
            if left in h: 
                h[left].append(right)
            else:
                h[left] = [right]

            if right in h: 
                h[right].append(left)
            else:
                h[right] = [left]


            
        def dfs(node, parent, visited):
            
            for i in h[node]:
                if i in visited and i != parent:
                    return [node,i]
            
            visited = visited + [node]


            for i in h[node]:
                if i == parent:
                    continue
                result = dfs(i, node, visited.copy())
                if result:
                    return result

        for i in h:
            val = dfs(i,i,[])
            if val:
                sol.append(val)

        ind = 0
        value = None
        for x,y in sol:
          
            first = [x,y]
            second = [y,x]

            if first in edges and edges.index(first) > ind:
                ind  = edges.index(first)
                value = first
            elif second in edges and edges.index(second) > ind:
                ind  = edges.index(second)
                value = second
        return value


        