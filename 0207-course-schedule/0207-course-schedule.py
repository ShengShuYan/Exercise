class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            indegree[a] += 1
            adj[b].append(a)
           
            # 2. 把所有入度=0的的节点放进队列
        from collections import deque
        queue = deque()
        for v in range(numCourses):
            if indegree[v] == 0:
                queue.append(v)
            
            # 3. 记录处理了多少个节点
        count = 0
            
            # 4. 开始处理
        while queue:
            v = queue.popleft()    # 出一个入度0的的节点
            count += 1                 # 计数+1
                
                # 5. 删除 v 出发的所有边 = 邻居入度-1
            for neighbor in adj[v]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)  # 新的入度0，入队
            
        return count == numCourses      

        