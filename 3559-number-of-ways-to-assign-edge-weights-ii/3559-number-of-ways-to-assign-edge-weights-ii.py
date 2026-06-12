from collections import defaultdict

class Solution:
    def assignEdgeWeights(self, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        n = len(edges) + 1
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # 1. 预处理：计算深度和二进制提升表
        LOG = 18  # 2^17 > 10^5
        depth = [0] * (n + 1)
        up = [[0] * LOG for _ in range(n + 1)]
        
        # 使用 BFS 或 DFS 填充深度和第 2^0 级祖先
        stack = [(1, 0, 0)]  # node, parent, d
        while stack:
            u, p, d = stack.pop()
            depth[u] = d
            up[u][0] = p
            for v in adj[u]:
                if v != p:
                    stack.append((v, u, d + 1))
        
        # 填充完整的二进制提升表
        for k in range(1, LOG):
            for i in range(1, n + 1):
                up[i][k] = up[up[i][k-1]][k-1]
        
        # 2. LCA 函数：在 O(log n) 时间内查找 LCA
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            # 将 u 提升到与 v 同深度
            for k in range(LOG - 1, -1, -1):
                if depth[u] - (1 << k) >= depth[v]:
                    u = up[u][k]
            if u == v:
                return u
            # 同时向上跳
            for k in range(LOG - 1, -1, -1):
                if up[u][k] != up[v][k]:
                    u = up[u][k]
                    v = up[v][k]
            return up[u][0]
        
        # 3. 处理查询
        MOD = 10**9 + 7
        ans = []
        for u, v in queries:
            lca = get_lca(u, v)
            dist = depth[u] + depth[v] - 2 * depth[lca]
            
            if dist == 0:
                ans.append(0)
            else:
                # 方案数公式：2^(dist-1)
                ans.append(pow(2, dist - 1, MOD))
        
        return ans