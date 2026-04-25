import bisect
class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        L = len(points)
        for i in range(L):
            x, y = points[i]
            if x == 0:
                points[i] = 4 * side - y
            elif x == side:
                points[i] = side + y
            elif y == 0:
                points[i] = x
            else:
                points[i] = 3 * side - x
        points.sort()
        TL = 4 * side
        arr = points + [x + TL for x in points]
        low = 1
        high = 4 * side // k
        ans = 1

        def check(D):
            for i in range(L):
                if points[i] > points[0] + D:
                    break
                
                count = 1
                lp = points[i]
                fp = points[i]

                idx = i
                for j in range(k-1):
                    tar = lp + D
                    idx = bisect.bisect_left(arr, tar, lo=idx + 1)
                    if idx >= i + L:
                        break
                    lp = arr[idx]
                    count += 1
                if count == k and (fp + TL - lp) >= D:
                    return True
            return False


        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans