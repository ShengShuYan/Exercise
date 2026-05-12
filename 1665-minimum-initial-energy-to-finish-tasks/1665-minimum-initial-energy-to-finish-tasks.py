class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: (-x[1] + x[0]))
        ans = max(tasks[0])
        cur = ans
        for a, m in tasks:
            if cur >= m:
                cur -= a
            else:
                ans += m - cur
                cur = m - a

        return ans
        