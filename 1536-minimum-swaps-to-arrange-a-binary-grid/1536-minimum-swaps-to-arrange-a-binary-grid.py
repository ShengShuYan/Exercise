class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        c0l = []
        for row in grid:
            i = n-1
            c0 = 0
            while i >= 0 and row[i] == 0:
                c0 += 1
                i -= 1
            c0l.append(c0)

        check = 0

        for i in range(n):
            need = n - i - 1
            j = i
            while j < n and c0l[j] < need:
                j += 1
            if j == n:
                return -1
            check += j - i
            val = c0l.pop(j)
            c0l.insert(i,val)


        return check       