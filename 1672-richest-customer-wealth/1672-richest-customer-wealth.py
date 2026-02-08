class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        wealth = [sum(accounts[i]) for i in range(len(accounts))]
        return max(wealth)


        