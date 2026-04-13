class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        cd = {}
        res = 200001
        for i in range(n):
            cv = nums[i]
            if cv not in cd:
                cd[cv] = [i]
            else:
                cd[cv].append(i)

        for ev in cd.values():
            l = len(ev)
            if l < 3:
                continue
            else:
                for i in range(l-2):
                    res = min((2 * (ev[i+2] - ev[i])), res)
        if res == 200001:
            return -1
        else:
            return res




        