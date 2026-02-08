# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.check(root) != -1

    def check(self, node: TreeNode) -> int:
        if not node:
            return 0
        
        leftH = self.check(node.left)
        if leftH == -1:
            return -1

        rightH = self.check(node.right)
        if rightH == -1:
            return -1

        if abs(leftH - rightH) > 1:
            return -1

        return max(leftH, rightH) + 1

        

        