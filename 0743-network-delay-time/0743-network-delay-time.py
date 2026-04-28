import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1. 建图：邻接表
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        
        # 2. 初始化：dist字典记录到每个点的最短时间，优先队列记录 (当前时间, 当前节点)
        # pq 存的是 (time, node)
        pq = [(0, k)]
        dist = {}
        
        while pq:
            time, u = heapq.heappop(pq)
            
            # 如果已经找到过该点的更短路径，跳过
            if u in dist:
                continue
            dist[u] = time
            
            # 遍历邻居
            for v, w in adj[u]:
                if v not in dist:
                    heapq.heappush(pq, (time + w, v))
        
        # 3. 结果判断
        # 如果收到的节点数等于 n，返回最晚接收到的时间；否则返回 -1
        return max(dist.values()) if len(dist) == n else -1
