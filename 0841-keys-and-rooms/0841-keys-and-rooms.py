class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {0}
        stack = [0] # Use a list as a stack for Iterative DFS
        
        while stack:
            u = stack.pop() # O(1) operation
            for v in rooms[u]:
                if v not in visited:
                    visited.add(v)
                    stack.append(v)
        
        return len(visited) == len(rooms)
