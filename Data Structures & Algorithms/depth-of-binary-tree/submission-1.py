# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0



        def dfs(node):
            if not node.left and not node.right:
                return 1 # the current depth

            
            left = 0
            right = 0
            if node.left:
                left = dfs(node.left) 
            if node.right:
                right = dfs(node.right)
            
            return max(left,right) + 1

        return dfs(root)

        