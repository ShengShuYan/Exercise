from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 1. 构造图
        graph = defaultdict(dict)
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0 / val
        
        # 2. 定义 DFS 函数
        def dfs(start, end, visited):
            # 如果走到了终点，返回 1.0（倍数之积的基数）
            if start == end:
                return 1.0
            
            visited.add(start)
            
            # 遍历邻居节点
            for neighbor, weight in graph[start].items():
                if neighbor not in visited:
                    res = dfs(neighbor, end, visited)
                    if res != -1.0:
                        return weight * res # 路径倍数累乘
            
            return -1.0 # 没找到路径

        # 3. 处理查询
        results = []
        for c, d in queries:
            if c not in graph or d not in graph:
                results.append(-1.0)
            else:
                results.append(dfs(c, d, set()))
        
        return results
