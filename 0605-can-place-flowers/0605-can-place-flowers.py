class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0: return True
        ans = 0
        l = len(flowerbed)
        if l == 1:
            return flowerbed[0] == 0
        for i in range(l):
            if ans >= n: return True
            if flowerbed[i] == 1:
                continue
            if i == 0:
                if flowerbed[1] == 0:
                    flowerbed[0] = 1
                    ans += 1
                continue
            elif flowerbed[i-1] == 1:
                continue
            elif i == l-1:
                flowerbed[i] = 1
                ans += 1
                continue
            elif flowerbed[i+1] == 0:
                flowerbed[i] = 1
                ans += 1
        return ans >= n
            
        