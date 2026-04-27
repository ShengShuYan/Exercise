class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.pre = -float('inf')

        def sinorder(node):
            if not node:
                return True
            
            # 如果左子树返回 False，向上层返回 False
            if not sinorder(node.left):
                return False
            
            # 比较当前值与前一个值
            if node.val <= self.pre:
                return False
            self.pre = node.val
            
            # 递归右子树并返回其结果
            return sinorder(node.right)
        
        return sinorder(root)
