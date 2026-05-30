from sortedcontainers import SortedList

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (2 * n)

    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i //= 2
            self.tree[i] = max(self.tree[2*i], self.tree[2*i+1])

    def query(self, l, r):
        l+=self.n
        r+= self.n
        res = 0
        while l <= r:
            if l%2 == 1:
                res = max(res, self.tree[l])
                l+= 1
            if r % 2 == 0:
                res = max(res, self.tree[r])
                r -= 1
            l //= 2
            r //= 2
        return res

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:

        max_x = max(q[1] for q in queries)

        st = SegmentTree(max_x + 1)
        obstacles = SortedList([0])

        res = []

        for q in queries:
            if q[0] == 1:
                x = q[1]

                idx = obstacles.bisect_right(x)
                prev_x = obstacles[idx - 1]

                st.update(x, x - prev_x)

                if idx < len(obstacles):
                    next_x = obstacles[idx]
                    st.update(next_x, next_x - x)

                obstacles.add(x)

            else:
                x = q[1]
                sz = q[2]

                idx = obstacles.bisect_right(x) - 1
                last_obstacle = obstacles[idx]

                edge_gap = x - last_obstacle

                max_gap = st.query(0, last_obstacle)

                res.append(max(edge_gap, max_gap) >= sz)

        return res

        