import heapq
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        cmp_i = {}
        cmp_f = {}
        for i in range(len(colors)):
            v = colors[i]
            if v not in cmp_i:
                cmp_i[v] = i
            cmp_f[v] = i
        ini2 = heapq.nsmallest(2, cmp_i.items(), key=lambda x: x[1])
        fin2 = heapq.nsmallest(2, cmp_f.items(), key=lambda x: -x[1])
        if ini2[0][0] != fin2[0][0]:
            return fin2[0][1] - ini2[0][1]
        else:
            return max(fin2[0][1]-ini2[1][1], fin2[1][1]-ini2[0][1])
            
        