class Solution(object):
    def judgeCircle(self, moves):
        if moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D'):
            return True
        return False
        