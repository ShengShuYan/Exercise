class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost): return -1
        stack = []
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

        if l == 1: return 0
        for i in range(l):
            if gas[i] > cost[i]:
                stack.append(i)

        for j in stack:
            pe = 0
            for add in range(l):
                ind = (j+add) % l
                pe += (gas[ind] - cost[ind])
                if pe < 0:
                    break
            if pe >= 0:
                return j

