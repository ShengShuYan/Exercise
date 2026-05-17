class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        queue = [start]
        n = len(arr)
        while queue:
            cur = queue.pop()
            visited.add(cur)
            v = arr[cur]
            if not v:
                return True
            right = cur + v
            if right < n and right not in visited: 
                queue.append(right)
            left = cur - v
            if left >= 0 and left not in visited: 
                queue.append(left)

        return False
        