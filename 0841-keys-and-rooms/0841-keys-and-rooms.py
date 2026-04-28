class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(u, visited, graph):
            visited.add(u)
            for v in graph[u]:
                if v not in visited:
                    dfs(v, visited, graph)

        visited = {0}
        dfs(0, visited, rooms)
        if len(visited) != len(rooms):
            return False
        return True

        