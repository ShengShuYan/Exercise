class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        ans = [['.'] * m for i in range(n)]
        for i in range(m):
            count = 0
            for j in range(n):
                if boxGrid[i][j] == '*':
                    ans[j][m-1-i] = '*'
                    if j > 0:
                        now = j - 1
                    while count > 0:
                        ans[now][m-1-i] = '#'
                        count -= 1
                        now -= 1
                elif boxGrid[i][j] == '#':
                    count += 1
            now = n - 1
            while count > 0:
                ans[now][m-1-i] = '#'
                count -= 1
                now -= 1
            
        return ans

        