# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # so the idea is that when you set the left you also give a max value that the sub nodes can never go more than if they go more than they are invlaid and for the right node the same thing occours but min 
        
        ''' i start it might node i validate my righ tand lleft; 
        i call the recurrence by passing is valid to the left node giving the curent value as the max 
        if left.right is grater than the max is is not valid if it is valid .  we are good we are allowed ot do recurrence on that right node however what is he max vlue we pased to that right node ? well it cannot be greater than teh root.  but its min left cannot be smaller than its rooth . so eahc node much have a min and max whell calling 
        of the inital root the min value for the right node is itself and the amx value of hte left is it slef 
        '''

        def isValid(max_,min_,root):
            if not root: # correct
                return True
                
            if root.val >= max_  or root.val <= min_: # correct
                return False
            
            return isValid(root.val,min_ ,root.left) and isValid(max_,root.val,root.right)

        return isValid(float('inf'), float('-inf'), root)


            
        