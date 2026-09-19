class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_x = max(candies)
        return [x+extraCandies>=max_x for x in candies]
        