class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        d = 0
        r = 0
        for c in moves:
            if c == 'L':
                d -= 1
            elif c == 'R':
                d += 1
            else:
                r += 1
        if d >= 0:
            return d + r
        else:
            return r - d

        