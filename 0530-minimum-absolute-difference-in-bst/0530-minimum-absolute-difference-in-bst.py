# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sinorder(self, root, arr):
        if not root:
            return None
        if root.left:
            self.sinorder(root.left, arr)
        arr.append(root.val)
        if root.right:
            self.sinorder(root.right, arr)
        return arr
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = []
        self.sinorder(root, arr)
        ans = arr[1] - arr[0]
        for i in range(1, len(arr) - 1):
            ans = min(ans, arr[i+1] - arr[i])
        return ans
        

        