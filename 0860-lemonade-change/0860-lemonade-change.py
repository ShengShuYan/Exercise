class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cur_5 = 0
        cur_10 = 0
        for c in bills:
            if c == 5:
                cur_5 += 1
            elif c == 10:
                if cur_5 < 1:
                    return False
                cur_5 -= 1
                cur_10 += 1
            else:
                if cur_10 and cur_5:
                    cur_10 -= 1
                    cur_5 -= 1
                elif cur_5 < 3:
                    return False
                else:
                    cur_5 -= 3

        return True
        