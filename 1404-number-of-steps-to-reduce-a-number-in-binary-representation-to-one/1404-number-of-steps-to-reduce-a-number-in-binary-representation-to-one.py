class Solution:
    def numSteps(self, s: str) -> int:
        s = int(s, 2)
        turns = 0
        while s != 1:
            if s & 1:
                s += 1
            else:
                s = s >> 1
            turns += 1

        return turns
        