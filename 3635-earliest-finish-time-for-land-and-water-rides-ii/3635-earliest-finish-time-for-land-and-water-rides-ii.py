class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        land_end = min(x + y for x, y in zip(landStartTime, landDuration))
        water_end = min(x + y for x, y in zip(waterStartTime, waterDuration))

        ans1 = min(max(land_end, ws) + wd for ws, wd in zip(waterStartTime, waterDuration))
        ans2 = min(max(water_end, ls) + ld for ls, ld in zip(landStartTime, landDuration))
        return min(ans1,ans2)
        