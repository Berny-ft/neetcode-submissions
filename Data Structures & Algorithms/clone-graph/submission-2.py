"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        graph = {}


        def dfs(node):

            if node.val in graph:
                copy = graph[node.val]
                return copy

            new_node = Node(node.val,None)
            graph[node.val] = new_node

            for i in node.neighbors:
                if i.val in graph:
                    new_node.neighbors.append(graph[i.val])
                else:
                    new_node.neighbors.append( dfs(i)  )

            return new_node

        return dfs(node)



