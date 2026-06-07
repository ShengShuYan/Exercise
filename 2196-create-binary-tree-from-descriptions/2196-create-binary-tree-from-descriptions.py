# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:

        v_pool = {}
        C = set()
        for p, c, i in descriptions:
            if c not in v_pool:
                v_pool[c] = TreeNode(c)
            if p not in v_pool:
                v_pool[p] = TreeNode(p)
            if i == 1:
                v_pool[p].left = v_pool[c]
            else:
                v_pool[p].right = v_pool[c]

            C.add(c)

        for p in v_pool:
            if p not in C:
                return v_pool[p]

            
        