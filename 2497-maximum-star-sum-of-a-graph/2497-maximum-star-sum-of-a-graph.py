from collections import defaultdict
import heapq

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        # 1. 初始值设为节点中的最大值（应对 k=0 或所有边收益为负的情况）
        ans = max(vals)
        if k == 0: return ans
        
        adj = defaultdict(list)
        for a, b in edges:
            # 只有当邻居为正数时，才考虑加入星形图
            if vals[b] > 0: adj[a].append(vals[b])
            if vals[a] > 0: adj[b].append(vals[a])

        for n in adj:
            # 使用 nlargest 比全排序在 k 较小时更快
            best_neighbors = heapq.nlargest(k, adj[n])
            ans = max(ans, vals[n] + sum(best_neighbors))
            
        return ans
