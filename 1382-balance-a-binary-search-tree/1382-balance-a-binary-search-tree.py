# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        arr = []

        def order(Node):
            if not Node:
                return
            order(Node.left)
            arr.append(Node.val)
            order(Node.right)

        order(root)

        def build(lf, rt):
            if lf > rt:
                return
            mid = (lf + rt) // 2
            root = TreeNode(arr[mid])

            root.left = build(lf, mid - 1)
            root.right = build(mid + 1, rt)

            return root     
        
        return build(0, len(arr) - 1)



        