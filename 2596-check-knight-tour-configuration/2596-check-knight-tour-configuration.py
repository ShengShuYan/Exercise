class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        # 如果起点不是左上角，直接返回 False
        if grid[0][0] != 0:
            return False
        
        n = len(grid)
        # 使用数组记录每个序号对应的坐标: pos[序号] = (r, c)
        pos = [None] * (n * n)
        for r in range(n):
            for c in range(n):
                pos[grid[r][c]] = (r, c)
        
        # 依次检查相邻两步是否符合马步规则
        for i in range(1, n * n):
            r1, c1 = pos[i-1]
            r2, c2 = pos[i]
            
            dx = abs(r1 - r2)
            dy = abs(c1 - c2)
            
            # 马步必须满足 1*2 或 2*1 的移动规律
            if not ((dx == 1 and dy == 2) or (dx == 2 and dy == 1)):
                return False
                
        return True
