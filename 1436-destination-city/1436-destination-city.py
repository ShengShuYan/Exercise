class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = set()
        out = set()
        for a, b in paths:
            cities.add(a)
            cities.add(b)
            out.add(a)

        dif = cities - out
        return dif.pop()

        