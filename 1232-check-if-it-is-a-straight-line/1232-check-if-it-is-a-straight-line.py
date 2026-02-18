class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        c0x = coordinates[0][0]
        c0y = coordinates[0][1]
        c1x = coordinates[1][0]
        c1y = coordinates[1][1]
        x0 = c1x - c0x
        y0 = c1y - c0y

        for x, y in coordinates:
            if x0 * (y - c0y) != y0 * (x - c0x):
                return False

        return True


        