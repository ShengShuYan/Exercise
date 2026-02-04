class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a = 0
        for i in digits:
            a = a*10+i
        b = [int(c) for c in str(a+1)]
        return b