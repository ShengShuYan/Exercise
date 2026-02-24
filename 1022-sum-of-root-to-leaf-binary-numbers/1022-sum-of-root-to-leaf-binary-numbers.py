# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode], fore = 0) -> int:
        if not root:
            return

        if not root.left and not root.right:
            return ((fore << 1) | root.val)

        fore = ((fore << 1) | root.val)

        tot = 0

        if root.left:
            tot += self.sumRootToLeaf(root.left, fore)

        if root.right:
            tot += self.sumRootToLeaf(root.right, fore)

        return tot
        