"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visit = {}

        def dfs(original):
            if original in visit:
                return visit[original]

            clone = Node(original.val)

            visit[original] = clone

            for neigh in original.neighbors:
                clone.neighbors.append(dfs(neigh))

            return clone

        return dfs(node)
        

        