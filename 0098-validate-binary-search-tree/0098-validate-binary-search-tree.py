# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.pre = -float('inf')

        def sinorder(node):
            if not node:
                return True
            if not sinorder(node.left):
                return False
            if node.val <= self.pre:
                return False
            self.pre = node.val
            return sinorder(node.right)
        
        
        return sinorder(root)

            
            


        