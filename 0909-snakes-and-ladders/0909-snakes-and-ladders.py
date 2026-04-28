from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        # 坐标转换辅助函数：将编号转换为矩阵的 (r, c)
        def get_pos(label):
            r, c = divmod(label - 1, n)
            row = n - 1 - r
            col = c if r % 2 == 0 else n - 1 - c
            return row, col

        queue = deque([(1, 0)])  # (当前编号, 步数)
        visited = {1}
        
        while queue:
            curr, steps = queue.popleft()
            
            for i in range(1, 7):
                nxt = curr + i
                if nxt > n * n: break
                
                r, c = get_pos(nxt)
                # 如果有蛇或梯子，传送；否则停在原地
                destination = board[r][c] if board[r][c] != -1 else nxt
                
                if destination == n * n:
                    return steps + 1
                
                if destination not in visited:
                    visited.add(destination)
                    queue.append((destination, steps + 1))
                    
        return -1
