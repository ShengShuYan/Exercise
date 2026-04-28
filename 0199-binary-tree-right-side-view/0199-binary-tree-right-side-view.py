from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        # 使用 deque 保证 popleft 为 O(1)
        queue = deque([root])
        
        while queue:
            # 记录当前层的节点数，用于区分层级
            level_size = len(queue)
            
            for i in range(level_size):
                # 必须用 popleft() 保持 FIFO（先进先出）
                node = queue.popleft()
                
                # 如果是当前层的最后一个节点，它就是右视图可见的节点
                if i == level_size - 1:
                    res.append(node.val)
                
                # 先加左再加右，确保每一层是从左到右排列的
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return res
