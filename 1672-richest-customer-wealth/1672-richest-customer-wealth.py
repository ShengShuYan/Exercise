class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        wealthy = 0
        for c in accounts:
            current = sum(c)
            wealthy = max(wealthy, current)
        return wealthy


        