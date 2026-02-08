class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        wealthy = 0
        for i in range(len(accounts)):
            current = sum(accounts[i])
            wealthy = max(wealthy, current)
        return wealthy


        