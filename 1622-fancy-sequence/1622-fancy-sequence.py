class Fancy:

    def __init__(self):
        self.sequence = []
        self.MOD = 10**9+7
        self.mul = 1
        self.add = 0
        

    def append(self, val: int) -> None:
        inv_mul = pow(self.mul, self.MOD - 2, self.MOD)
        self.sequence.append(((val - self.add) * inv_mul) % self.MOD)
        

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        
        if idx >= len(self.sequence):
            return -1
        return (self.sequence[idx] * self.mul + self.add) % self.MOD
        


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)