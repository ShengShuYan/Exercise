from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. 建立邻接表和入度表
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        
        for cur, pre in prerequisites:
            adj[pre].append(cur)
            indegree[cur] += 1
            
        # 2. 将所有入度为 0 的节点（没有先修课的课）入队
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        visited_count = 0
        while queue:
            pre = queue.popleft()
            visited_count += 1
            
            # 3. 遍历当前课的所有后续课
            for cur in adj[pre]:
                indegree[cur] -= 1
                # 如果后续课的入度减为 0，说明它的先修课都上完了
                if indegree[cur] == 0:
                    queue.append(cur)
        
        # 4. 如果上过的课等于总数，说明没有环
        return visited_count == numCourses
