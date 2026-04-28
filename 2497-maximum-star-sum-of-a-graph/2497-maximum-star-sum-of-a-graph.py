from collections import defaultdict
class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        if not edges:
            return max(vals)
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(vals[b])
            adj[b].append(vals[a])

        ans = -float('inf')
        for n, c in adj.items():
            c.sort(reverse = True)
            cur = vals[n]
            i = 0
            while i < min(k,len(c)) and c[i] > 0:
                cur += c[i]
                i += 1
            ans = max(ans, cur)
        return max(ans, max(vals))
        