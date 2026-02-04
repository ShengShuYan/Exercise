class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        L = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        i = 0
        _ = [0, 0]
        for c in instructions:
            if c == 'L':
                i += 1
                i = i % 4
            elif c == 'R':
                i -= 1
                i = i % 4
            else:
                _ = [_[0] + L[i][0], _[1] + L[i][1]]
        return _ == [0, 0] or i != 0


            
        