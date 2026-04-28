from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        start_r, start_c = entrance
        
        # 队列存储 (行, 列, 步数)
        queue = deque([(start_r, start_c, 0)])
        # 将起点设为墙，防止走回头路
        maze[start_r][start_c] = '+'
        
        while queue:
            curr_r, curr_c, dist = queue.popleft()
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = curr_r + dr, curr_c + dc
                
                # 检查是否越界且是空地
                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == '.':
                    # 检查是否是出口（在边界上）
                    if nr == 0 or nr == m - 1 or nc == 0 or nc == n - 1:
                        return dist + 1
                    
                    # 标记并加入队列
                    maze[nr][nc] = '+'
                    queue.append((nr, nc, dist + 1))
        
        return -1
