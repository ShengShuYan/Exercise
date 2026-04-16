from collections import defaultdict
from bisect import bisect_left

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        N = len(queries)
        LN = len(nums)
        numdict = defaultdict(list)
        for ind, val in enumerate(nums):
            numdict[val].append(ind)
        
        out = []
        
        for q in queries:
            cl = numdict[nums[q]]
            cl_l = len(cl)
            if len(cl) == 1:
                out.append(-1)
            else:
                indn = bisect_left(cl, q)
                pre = cl[(indn-1)%cl_l]
                pos = cl[(indn+1)%cl_l]
                df = min(abs(q-pre), LN-abs(pre-q))
                da = min(abs(pos - q), LN-abs(pos-q))
                out.append(min(df,da))

        return out


        