from collections import defaultdict
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:

        parent = defaultdict(list)

        for u, v in edges:
            parent[u].append(v)
            parent[v].append(u)

        deep = 0
        stack = [(1, 0)]
        visited = {1}

        while stack:
            node, depth = stack.pop()
            deep = max(deep, depth)
            for child in parent[node]:
                if child not in visited:
                    visited.add(child)
                    stack.append((child, depth + 1))            
            
        return pow(2, deep-1, 10**9 + 7)
        