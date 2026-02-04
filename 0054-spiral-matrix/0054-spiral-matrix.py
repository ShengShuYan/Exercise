class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        r = []
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = 0
        while 1:
            for _1 in range(n):
                r.append(matrix[i][j])
                j += 1
            j -= 1
            m -= 1
            if m == 0:
                break
            for _2 in range(m):
                i += 1
                r.append(matrix[i][j])
            n -= 1
            if n == 0:
                break
            for _3 in range(n):
                j -= 1
                r.append(matrix[i][j])
            m -= 1
            if m == 0:
                break
            for _4 in range(m):
                i -= 1
                r.append(matrix[i][j])
            n -= 1
            if n == 0:
                break
            j += 1
        # if m < n:
        #     for _5 in range(n):
        #         r.append(matrix[t+_5][m])
        # else:
        #     for _5 in range(m):
        #         r.append(matrix[n][t+_5])
        return r

            

                



        