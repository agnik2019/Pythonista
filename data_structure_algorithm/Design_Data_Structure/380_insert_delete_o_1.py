class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        res = val not in self.map
        if res:
            self.map[val] = len(self.arr)
            self.arr.append(val)        
        return res

    def remove(self, val: int) -> bool:
        res = val in self.map
        if res:
            idx = self.map[val]
            lastval = self.arr[-1]
            self.arr[idx] = lastval
            self.arr.pop()
            self.map[lastval] = idx
            del self.map[val]     
        return res
        

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()