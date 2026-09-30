class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        dep1 = 0
        dep2 = 0
        ans = []
        for s in seq:
            if s == '(':
                if dep1<=dep2:
                    dep1 += 1
                    ans.append(0)
                else:
                    dep2 += 1
                    ans.append(1)
            else:
                if dep1>=dep2:
                    dep1 -= 1
                    ans.append(0)
                else:
                    dep2 -= 1
                    ans.append(1)
        return ans

