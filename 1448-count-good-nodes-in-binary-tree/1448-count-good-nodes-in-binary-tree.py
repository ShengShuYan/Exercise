# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def judge(node, val):
            if not node:
                return 0
            
            ans = 1 if node.val >= val else 0

            val = max(val, node.val)

            ans += judge(node.left, val)
            ans += judge(node.right, val)

            return ans

        return judge(root, root.val)

        

        