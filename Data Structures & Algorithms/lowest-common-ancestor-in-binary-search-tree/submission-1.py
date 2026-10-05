# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # you must explore the tree until it branches in such a way that that the two nodes canot be in teh same branch 
        # that branching point is the LCA
        # so keep going recursively until you reach a point where oen goes to the right and the other goes to the left 
        # or all combinations of that or one is the current node and the nother goes on eithe rdies 

        q_val = q.val
        p_val = p.val
        
        def lowest(root):
            # there is not edge case where we find no sol
            if root == p or root == q:
                return root
            
            if p_val < root.val and q.val < root.val:
                return lowest(root.left)
            elif p_val > root.val and q.val > root.val:
                return lowest(root.right)
            else: # they'e branched
                return root

        
        return lowest(root)
        