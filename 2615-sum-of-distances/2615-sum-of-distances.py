from collections import defaultdict
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        mapd = defaultdict(list)
        for i in range(len(nums)):
            mapd[nums[i]].append(i)
        arr = [0] * len(nums)
        for v in mapd.values():
            start = v[0]
            L = len(v)
            arr[start] = sum(v) - start * L
            sv = arr[start]
            for ind in range(1, len(v)):
                arr[v[ind]] = sv + (2*ind-L) * (v[ind] - v[ind-1])
                sv = arr[v[ind]]

        return arr
