class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # so does valididity mean connected and acyclic

        # we first build the adjacency list
        if len(edges) != n-1:
            return False

        h = {}
        for left,right in edges:
            if left in h:
                h[left].append(right)
            else:
                h[left] = [right]
            
            if right in h:
                h[right].append(left)
            else:
                h[right] = [left]

        def dfs(node,parent,visited):
            if node in visited: 
                return False
            
            visited.append(node)

           
            for i in h.get(node,[]):
                if i == parent:
                    continue
                if not dfs(i, node, visited):
                    return False

            return True

        visited = []
        state =  dfs(0,-1,visited)
        return True if len(visited) == n and state else False




