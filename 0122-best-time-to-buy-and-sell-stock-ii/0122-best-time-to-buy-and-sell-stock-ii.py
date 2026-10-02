class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l = len(prices)
        if l == 1: return 0
        if l == 2: return max(prices[1] - prices[0], 0)
        cmin = min(prices[0], prices[1])
        ans = 0
        for i in range(2, l):
            v = prices[i]
            fore = prices[i-1]
            if fore > cmin and v < fore:
                ans += fore - cmin
                cmin = v
            else:
                cmin = min(cmin, v)
        if prices[l-1] > cmin: ans += prices[l-1] - cmin
        return ans
        