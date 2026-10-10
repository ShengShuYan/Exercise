class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost): return -1
        l = len(gas)
        newl = [gas[i] - cost[i] for i in range(l)]
        index = -1
        comp = float('inf')
        at = 0
        for j in range(l):
            at += newl[j]
            if at < comp:
                comp = at
                index = j
        return (index+1)%l