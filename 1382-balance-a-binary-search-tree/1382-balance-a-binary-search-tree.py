# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def order(Node, arr):
            if not Node:
                return
            order(Node.left, arr)
            arr.append(Node.val)
            order(Node.right, arr)

        def build(arr, left, right):
            if left > right:
                return
            mid = (left + right) // 2
            root = TreeNode(arr[mid])

            root.left = build(arr, left, mid - 1)
            root.right = build(arr, mid + 1, right)

            return root

        arr = []
        order(root, arr)
        return build(arr, 0, len(arr) - 1)



        