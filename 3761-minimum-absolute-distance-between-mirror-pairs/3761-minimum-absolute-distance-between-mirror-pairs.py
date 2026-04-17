class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        last_seen = {}
        mind = float('inf')
        found = False

        for j, x in enumerate(nums):
            re = int(str(x)[::-1])

            if x in last_seen:
                i = last_seen[x]
                mind = min(mind, j-i)
                found = True

            last_seen[re] = j

        return mind if found else -1
