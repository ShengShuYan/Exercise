class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        leng = target[-1]
        target = set(target)
        out = []
        for i in range(1, leng+1):
            if i in target:
                out.append("Push")
            else:
                out.append('Push')
                out.append('Pop')

        return out


        