class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        leng = target[-1]
        ans = [0] * leng
        for i in target:
            ans[i-1] = 1
        out = []
        for j in ans:
            if j == 1:
                out.append("Push")
            else:
                out.extend(["Push", "Pop"])

        return out
        

        