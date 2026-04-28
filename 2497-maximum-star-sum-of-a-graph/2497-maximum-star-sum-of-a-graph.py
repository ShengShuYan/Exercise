from collections import defaultdict
class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        if not edges:
            return max(vals)
        adj = defaultdict(list)
        for a, b in edges:
            if vals[b] > 0:
                adj[a].append(vals[b])
            if vals[a] > 0:
                adj[b].append(vals[a])

        ans = -float('inf')
        for n, c in adj.items():
            c.sort(reverse = True)
            cur = vals[n]
            ans = max(ans, cur+sum(c[:min(k,len(c))]))
        return max(ans, max(vals))
        