class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        L = len(queries[0])
        for q in queries:
            for d in dictionary:
                dif = 0
                for i in range(L):
                    if q[i] != d[i]:
                        dif += 1
                    if dif > 2:
                        break
                if dif <= 2:
                    ans.append(q)
                    break
        return ans
                