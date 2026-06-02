class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        land = [(x, y, x+y) for x, y in zip(landStartTime, landDuration)]
        water = [(x, y, x+y) for x, y in zip(waterStartTime, waterDuration)]

        land.sort(key = lambda x: x[2])
        water.sort(key = lambda x: x[2])

        i = 0
        ans1 = float('inf')
        im = len(water)
        le = land[0][2]
        while i<im:
            cur = max(le, water[i][0]) + water[i][1]
            if ans1 > cur:
                ans1 = cur
            i +=  1
        
        j = 0
        ans2 = float('inf')
        jm = len(land)
        we = water[0][2]
        while j<jm:
            cur = max(we, land[j][0]) + land[j][1]
            if ans2 > cur:
                ans2 = cur
            j +=  1

        return min(ans1, ans2)
        