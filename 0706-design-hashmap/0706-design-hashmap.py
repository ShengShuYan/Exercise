class MyHashMap:

    def __init__(self):
        self.val = {}        

    def put(self, key: int, value: int) -> None:
        self.val[key] = value
        
    def get(self, key: int) -> int:
        if key not in self.val:
            return -1
        else:
            return self.val[key]

    def remove(self, key: int) -> None:
        if key in self.val:
            del self.val[key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)