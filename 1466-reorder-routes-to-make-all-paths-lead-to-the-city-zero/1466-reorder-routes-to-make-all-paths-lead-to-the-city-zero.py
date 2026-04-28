class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for a, b in connections:
            adj[a].append((b, 1))
            adj[b].append((a, 0))

        ans = 0
        visited = {0}
        stack = [0]

        while stack:
            c = stack.pop()
            for n, cost in adj[c]:
                if n not in visited:
                    stack.append(n)
                    visited.add(n)
                    ans += cost
                
        return ans