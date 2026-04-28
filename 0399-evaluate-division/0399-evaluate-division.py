class Solution:
    def calcEquation(self, equations, values, queries):
        root = {} # 存储父节点
        dist = {} # 存储 node / parent_node 的比例

        def find(i):
            if i not in root:
                root[i], dist[i] = i, 1.0
            if root[i] != i:
                orig_parent = root[i]
                root[i] = find(orig_parent) # 路径压缩
                dist[i] *= dist[orig_parent] # 更新比例：node / root
            return root[i]

        def union(i, j, v):
            root_i, root_j = find(i), find(j)
            if root_i != root_j:
                root[root_i] = root_j
                # 原理：i/root_i = dist_i, j/root_j = dist_j, i/j = v
                # 推导：root_i / root_j = (i / dist_i) / (j / dist_j) = v * dist_j / dist_i
                dist[root_i] = v * dist[j] / dist[i]

        # 1. 建并查集
        for (i, j), v in zip(equations, values):
            union(i, j, v)

        # 2. 查询
        res = []
        for i, j in queries:
            if i not in root or j not in root or find(i) != find(j):
                res.append(-1.0)
            else:
                # i / j = (i / root) / (j / root)
                res.append(dist[i] / dist[j])
        return res
