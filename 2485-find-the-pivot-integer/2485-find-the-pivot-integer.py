from math import sqrt
class Solution:
    def pivotInteger(self, n: int) -> int:
        ans = sqrt((n**2+n)/2)
        if ans.is_integer():
            return int(ans)
        return -1
        