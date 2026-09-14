class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x11, y11, x12, y12 = rec1
        x21, y21, x22, y22 = rec2
        if x12 <= x21 or x22 <= x11:
            return False
        if y12<=y21 or y22<=y11:
            return False
        return True