class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        parent = defaultdict(list)

        for u, v in edges:
            if u < v:
                parent[u].append(v)
            else:
                parent[v].append(u)

        depth = {}

        def get_depth(node):
            if node not in parent:
                return 0
            if node in depth:
                return depth[node]

            deep = 0
            for child in parent[node]:
                deep = max(deep, 1+get_depth(child))

            depth[node] = deep
            return deep

        ans = get_depth(1)
            
        return pow(2, ans-1, 10**9 +7)
        