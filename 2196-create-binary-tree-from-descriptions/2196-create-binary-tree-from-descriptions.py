# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        P = set()
        C = set()
        v_pool = {}
        for p, c, i in descriptions:
            if c not in v_pool:
                v_pool[c] = TreeNode(c)
            if p not in v_pool:
                if i == 1:
                    v_pool[p] = TreeNode(p, v_pool[c])
                else:
                    v_pool[p] = TreeNode(p, None, v_pool[c])
            else:
                if i == 1:
                    v_pool[p].left = v_pool[c]
                else:
                    v_pool[p].right = v_pool[c]
            P.add(p)
            C.add(c)

        for p in P:
            if p not in C:
                return v_pool[p]

            
        