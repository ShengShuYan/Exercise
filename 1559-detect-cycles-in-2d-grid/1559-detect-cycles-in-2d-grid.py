from typing import List
from collections import defaultdict

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # 按值分组
        value_to_cells = defaultdict(list)
        for i in range(m):
            for j in range(n):
                value_to_cells[grid[i][j]].append((i, j))
        
        # 对每个值，用并查集检测环
        for val, cells in value_to_cells.items():
            if len(cells) < 4:
                continue
            
            # 编号: i*n + j
            parent = {}
            
            def find(x):
                if x not in parent:
                    parent[x] = x
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]
            
            def union(x, y):
                px, py = find(x), find(y)
                if px == py:
                    return False  # 已经在同一集合，形成环！
                parent[px] = py
                return True
            
            # 遍历所有同值相邻边
            cell_set = set(cells)
            for i, j in cells:
                for dx, dy in [(-1,0), (1,0), (0,1), (0,-1)]:
                    ni, nj = i + dx, j + dy
                    if (ni, nj) in cell_set:
                        u, v = i * n + j, ni * n + nj
                        # 只处理一次（避免重复）
                        if u < v:
                            if not union(u, v):
                                return True
        
        return False