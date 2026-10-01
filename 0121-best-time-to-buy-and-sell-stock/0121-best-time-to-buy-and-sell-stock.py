class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        ans = 0
        cmin = prices[0]
        for p in prices:
            cmin = min(cmin, p)
            ans = max(p-cmin, ans)
        return ans
