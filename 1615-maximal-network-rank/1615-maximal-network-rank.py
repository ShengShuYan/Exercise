class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        deg = [0] * n
        adj = set()
        for a, b in roads:
            deg[a] += 1
            deg[b] += 1
            adj.add(tuple(sorted((a,b))))
        
        mdeg = sorted(set(deg), reverse = True)
        maxdeg = mdeg[0]
        secdeg = mdeg[1] if len(mdeg) > 1 else 0

        first = [i for i, d in enumerate(deg) if d == maxdeg]
        second = [j for j, d in enumerate(deg) if d == secdeg]

        if len(first) > 1:
            for i in range(len(first)):
                for j in range(i+1, len(first)):
                    if (first[i], first[j]) not in adj:
                        return 2 * maxdeg
            return 2 * maxdeg - 1

        f = first[0]
        for c in second:
            if tuple(sorted((f, c))) not in adj:
                return maxdeg + secdeg
        return maxdeg + secdeg - 1


        