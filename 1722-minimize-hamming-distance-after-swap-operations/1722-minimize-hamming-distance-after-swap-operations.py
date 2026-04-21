class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))

        def find(i):
            if parent[i] == i: return i
            parent[i] = find(parent[i])
            return parent[i]

        for a, b in allowedSwaps:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
            
        groups = collections.defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)
        
        res = 0
        for ind in groups.values():
            count = collections.Counter(source[i] for i in ind)
            match = 0
            for i in ind:
                if count[target[i]] > 0:
                    match += 1
                    count[target[i]] -= 1
            res += (len(ind) - match)

        return res

        