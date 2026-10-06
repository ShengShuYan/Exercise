class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort()
        h = 0
        while citations and citations[-1] >= h + 1:
            citations.pop()
            h += 1
        return h
        