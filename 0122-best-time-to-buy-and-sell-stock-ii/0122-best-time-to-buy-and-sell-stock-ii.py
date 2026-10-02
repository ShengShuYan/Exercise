class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l = len(prices)
        if l == 1: return 0
        cmin = prices[0]
        ans = 0
        for i in range(1, l):
            v = prices[i]
            if v > cmin:
                ans += v - cmin
            cmin = v
        return ans
        